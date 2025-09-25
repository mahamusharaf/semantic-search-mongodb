from sentence_transformers import SentenceTransformer
from pymongo import MongoClient
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')
client=MongoClient("mongodb://localhost:27017/")
db=client["time_machine_db"]
collection=db["books"]

queries = [
    "physical appearance of the time machine",
    "journey to the distant future",
    "lifestyle and characteristics of the Eloi",
    "Morlocks as subterranean creatures",
    "time as the fourth dimension"
]

query_embed=model.encode(queries)
docs=collection.find({},{"_id": 0, "sentence": 1,"embedding": 1})
sentence_db=[]
embedding_db=[]

for doc in docs:
    sentence_db.append(doc["sentence"])
    embedding_db.append(doc["embedding"])
embedding_db=np.array(embedding_db)

for i in range(len(queries)):
    query = queries[i]
    query_emb = query_embed[i]
    similarities = cosine_similarity([query_emb], embedding_db)[0]
    top_indices = similarities.argsort()[::-1][:3]
    print("\nQuery:", query)
    for idx in top_indices:
        print("  ->", sentence_db[idx], "(score=", round(similarities[idx], 4), ")")

