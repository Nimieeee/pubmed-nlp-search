# example.py
from pubmed_client import PubMedClient
from entity_relation import EntityRelationExtractor
from semantic_search import SemanticSearch
from relation_search import RelationSearch


def main():
    print("🔎 Fetching PubMed articles on antidepressant hepatotoxicity...")
    client = PubMedClient(email="your_email@example.com")
    abstracts, ids = client.fetch("antidepressant hepatotoxicity", retmax=5)

    extractor = EntityRelationExtractor()

    all_relations = []
    for pmid, abs_text in zip(ids, abstracts):
        entities, relations = extractor.extract(abs_text, pmid)
        print(f"\n📄 PMID {pmid}")
        print("Entities:", entities)
        print("Relations:", relations)
        all_relations.extend(relations)

    # ---- Semantic search over abstracts ----
    print("\n🔍 Semantic search demo (abstracts):")
    ss = SemanticSearch(abstracts)
    results = ss.search("SSRI-induced liver toxicity", top_k=3)
    for score, text in results:
        print(f"Score {score:.4f} → {text[:80]}...")

    # ---- Semantic search over relations ----
    print("\n🔍 Relation-level semantic search:")
    rs = RelationSearch()
    rel_results = rs.score_relations(all_relations, "hepatitis caused by SSRIs")

    for rel_text, score, pmid in rel_results[:5]:
        print(f"Score {score:.4f} → {rel_text} (PMID {pmid})")


if __name__ == "__main__":
    main()
