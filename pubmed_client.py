from Bio import Entrez

class PubMedClient:
    def __init__(self, email):
        Entrez.email = email

    def fetch(self, query, retmax=10):
        handle = Entrez.esearch(db="pubmed", term=query, retmax=retmax)
        record = Entrez.read(handle)
        ids = record["IdList"]

        abstracts = []
        for pmid in ids:
            fetch = Entrez.efetch(db="pubmed", id=pmid, rettype="abstract", retmode="text")
            abstracts.append(fetch.read())
        return abstracts, ids
