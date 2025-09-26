# semantic-search-mongodb
This project demonstrates how to perform semantic search on text from books (sourced from Project Gutenberg). We compare two storage and search approaches:
- MongoDB (traditional database + cosine similarity search in Python)
- Qdrant (vector database optimized for similarity search)

**Workflow**:
- Download a book (e.g., The Time Machine by H.G. Wells) from Project Gutenberg.
- Extracted one chapter for testing.
- Break chapters into individual sentences using NLTK.
- Convert each sentence into a vector (embedding) using a HuggingFace model.
  
**Model Used**:
We used the HuggingFace Sentence Transformers model:
 - sentence-transformers/all-MiniLM-L6-v2
 - Embedding Dimension: 384
 - Optimized for semantic similarity and sentence-level search
 - Lightweight and fast, ideal for experimentation
   
**MongoDB Approach**:
-Store embeddings + sentences in a books collection.
For queries:
-Convert query → embedding
-Compute cosine similarity with stored embeddings using NumPy.
-Return top results.

**Qdrant Approach**:
- Run Qdrant locally via Docker.
- Store embeddings in a Qdrant collection with payloads (sentences).
For queries:
- Convert query → embedding
- Use Qdrant’s vector search API to fetch most similar results.

**Comparison**
- MongoDB: Works fine but requires manual cosine similarity computation in Python (slower for large datasets).
- Qdrant: Purpose-built for vector similarity → faster, scalable, and has filtering features.
