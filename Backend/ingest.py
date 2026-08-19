import chromadb
from embedding import embed

client = chromadb.PersistentClient(path="./chroma_store")
collection = client.get_or_create_collection("email_style")

def ingest_emails(emails: list[str]):
    for i, email in enumerate(emails):
        collection.add(
            ids=[f"email_{i}"],
            embeddings=[embed(email)],
            documents=[email],
        )