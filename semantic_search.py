# semantic_search.py
from sentence_transformers import SentenceTransformer
from annoy import AnnoyIndex

class SemanticSearch:
    def __init__(self, corpus, embedder="all-MiniLM-L6-v2", n_trees=10):
        self.embedder = SentenceTransformer(embedder)
        self.corpus = corpus
        self.embeddings = self.embedder.encode(corpus, show_progress_bar=True)

        self.dim = self.embeddings.shape[1]
        self.index = AnnoyIndex(self.dim, metric="angular")

        for i, vec in enumerate(self.embeddings):
            self.index.add_item(i, vec.tolist())
        self.index.build(n_trees)

    def search(self, query, top_k=3):
        q_vec = self.embedder.encode([query])[0]
        ids, scores = self.index.get_nns_by_vector(q_vec, top_k, include_distances=True)
        results = []
        for idx, dist in zip(ids, scores):
            results.append((1 - dist, self.corpus[idx]))  # cosine ≈ 1 - angular
        return results
