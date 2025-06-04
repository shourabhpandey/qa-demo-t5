from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import re

class Retriever:
    def __init__(self):
        self.embedder = SentenceTransformer('all-MiniLM-L6-v2')
        self.index = None
        self.chunks = []

    def split_text(self, text, chunk_size=512, overlap=50):
        sentences = re.split(r'(?<=[.?!])\s+', text)
        chunks = []
        chunk = ""
        for sentence in sentences:
            if len(chunk) + len(sentence) <= chunk_size:
                chunk += " " + sentence
            else:
                chunks.append(chunk.strip())
                chunk = sentence
        if chunk:
            chunks.append(chunk.strip())

        # Add overlap
        final_chunks = []
        for i in range(0, len(chunks)):
            start = max(0, i - 1)
            merged = " ".join(chunks[start:i+1])
            final_chunks.append(merged)
        return final_chunks

    def add_text(self, text):
        new_chunks = self.split_text(text)
        new_embeddings = self.embedder.encode(new_chunks)
        self.chunks += new_chunks

        if self.index is None:
            dim = new_embeddings.shape[1]
            self.index = faiss.IndexFlatL2(dim)

        self.index.add(np.array(new_embeddings))

    def retrieve(self, query, top_k=3):
        query_embedding = self.embedder.encode([query])
        D, I = self.index.search(np.array(query_embedding), top_k)
        return [self.chunks[i] for i in I[0]]
