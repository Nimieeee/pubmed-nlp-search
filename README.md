# PubMed NLP Search 🔎🧪

[![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-Models-yellow)](https://huggingface.co/models)
[![PubMed](https://img.shields.io/badge/Data-PubMed-green)](https://pubmed.ncbi.nlm.nih.gov/)
[![License: MIT](https://img.shields.io/badge/License-MIT-lightgrey.svg)](LICENSE)

A hybrid NLP pipeline for exploring biomedical literature.  
It combines **semantic search** over PubMed abstracts with **relation-level search** using PubMedBERT.  
The goal is to make it easier to find relevant biomedical knowledge (e.g., drug–disease relations) from PubMed.

---

## 🚀 Features
- **PubMed Fetching** – fetch abstracts directly from PubMed using `Biopython`.
- **Entity & Relation Extraction** – extract biomedical entities (via SciSpacy / BioNER) and generate candidate relations.
- **Semantic Search** – search across abstracts using `all-MiniLM-L6-v2`.
- **Relation Search** – score extracted relations with `S-PubMedBERT-MS-MARCO`.

---

## 📂 Project Structure
```
pubmed-nlp-search/

│── example.py # Example pipeline (run this first)

│── semantic_search.py # Abstract-level semantic search (MiniLM + Annoy)

│── relation_search.py # Relation-level semantic search (PubMedBERT)

│── entity_relation.py # Simple entity & relation extractor

│── pubmed_client.py # Fetches abstracts from PubMed

│── requirements.txt # Python dependencies

│── README.md # This file
```

---

## ⚙️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/Nimieeee/pubmed-nlp-search.git
cd pubmed-nlp-search

2. Create and activate a virtual environment
conda create -n pubmed-nlp python=3.9 -y
conda activate pubmed-nlp

3. Install dependencies
pip install -r requirements.txt

4. Install SciSpacy model (for biomedical entity extraction)
pip install https://s3.amazonaws.com/allenai-scispacy/releases/v0.5.1/en_core_sci_sm-0.5.1.tar.gz
```

▶️ Usage

Run the demo script:
```
python example.py
```
```
Example Output
🔎 Fetching PubMed articles on antidepressant hepatotoxicity...
📄 PMID 12345678
Entities: [('fluoxetine', 'CHEMICAL'), ('hepatitis', 'DISEASE')]
Relations: fluoxetine (CHEMICAL) → hepatitis (DISEASE)

🔍 Semantic search demo (abstracts):
Score 0.8123 → Antidepressant-induced hepatotoxicity is rare but serious...

🔍 Relation-level semantic search:
Score 0.9031 → fluoxetine (CHEMICAL) → hepatitis (DISEASE) (PMID 12345678)
```

📖 Requirements

Python 3.9+

PyTorch

SentenceTransformers

Transformers

SciSpacy

Biopython

📌 Notes

Models are not included in this repo (they are large). HuggingFace Hub will download them automatically on first use.
If you want to use custom models, update the model names in:

semantic_search.py → all-MiniLM-L6-v2

relation_search.py → pritamdeka/S-PubMedBERT-MS-MARCO

Large files should be handled via Git LFS.

✨ Future Work
Improve relation extraction (currently a simple heuristic).
Add support for entity normalization with MeSH / UMLS.
