from sentence_transformers import SentenceTransformer
from pymongo import MongoClient
import numpy as np
from extract import sentences

model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(sentences)
print(f"Generated embeddings for {len(sentences)} sentences.")

client = MongoClient("mongodb://localhost:27017")
db=client["time_machine_db"]
collection=db["books"]

documents = []
for sentence, embedding in zip(sentences, embeddings):
    documents.append({
        "sentence": sentence,
        "embedding": embedding.tolist()
    })
collection.insert_many(documents)
print(f"Successfully added {len(documents)} sentences to the MongoDB collection 'books'.")
