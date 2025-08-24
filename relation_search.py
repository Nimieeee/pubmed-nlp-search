# relation_search.py
from sentence_transformers import SentenceTransformer, util

class RelationSearch:
    def __init__(self, model_name="pritamdeka/S-PubMedBERT-MS-MARCO"):
        self.model = SentenceTransformer(model_name)

    def score_relations(self, relations_with_pmids, query, top_k=5):
        """
        relations_with_pmids = list of tuples: [(relation_text, pmid), ...]
        query = string query
        """
        relation_texts = [r[0] for r in relations_with_pmids]
        pmids = [r[1] for r in relations_with_pmids]

        # Embed
        query_emb = self.model.encode(query, convert_to_tensor=True)
        rel_embs = self.model.encode(relation_texts, convert_to_tensor=True)

        # Cosine similarity
        scores = util.cos_sim(query_emb, rel_embs)[0].cpu().tolist()

        # Bundle with PMIDs
        results = list(zip(relation_texts, scores, pmids))
        results.sort(key=lambda x: x[1], reverse=True)
        return results[:top_k]
