# entity_relation.py
from transformers import pipeline

class EntityRelationExtractor:
    def __init__(self, model="d4data/biomedical-ner-all"):
        self.ner = pipeline("ner", model=model, aggregation_strategy="simple")

    def extract(self, text, pmid="UNKNOWN"):
        ents = self.ner(text)
        entities = [(e['word'], e['entity_group']) for e in ents]

        # Very simple relation heuristic
        relations = []
        for i in range(len(entities) - 1):
            e1, t1 = entities[i]
            e2, t2 = entities[i + 1]
            relation_text = f"{e1} ({t1}) → {e2} ({t2})"
            relations.append((relation_text, pmid))

        return entities, relations
