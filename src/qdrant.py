from qdrant_client import QdrantClient
from qdrant_client.http import models
from sentence_transformers import SentenceTransformer
import numpy as np
from extract import sentences

client = QdrantClient(host="localhost", port=6333)
model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(sentences)

collection_name = "time_machine"
client.recreate_collection(
    collection_name=collection_name,
    vectors_config=models.VectorParams(
        size=embeddings.shape[1],
        distance=models.Distance.COSINE
    )
)
points = []
for i, (sentence, emb) in enumerate(zip(sentences, embeddings)):
    point = models.PointStruct(
        id=i,
        vector=emb.tolist(),
        payload={"sentence": sentence}
    )
    points.append(point)
client.upsert(
    collection_name=collection_name,
    points=points
)

print(f"Uploaded {len(points)} sentences to Qdrant.")
queries = [
    "the description of the time machine",
    "journey to the distant future",
    "lifestyle and characteristics of the Eloi",
    "Morlocks as subterranean creatures",
    "time as the fourth dimension"
]

query_embeddings = model.encode(queries)
for q in queries:
    q_emb = model.encode(q).tolist()
    results = client.search(collection_name=collection_name, query_vector=q_emb, limit=3)
    print(f"\nQuery: {q}")
    for r in results:
        print(f"  -> {r.payload['sentence']} (score={r.score:.4f})")