import json
from ingest import ingest_emails

def load_corpus(path: str) -> list[str]:
    emails = []
    with open(path, "r") as f:
        for line in f:
            record = json.loads(line)
            emails.append(record["body"])  # adjust key to your jsonl schema
    return emails

if __name__ == "__main__":
    emails = load_corpus("corpus.jsonl") # emails file where each line is a json object with a "body" field
    ingest_emails(emails)
    print(f"Ingested {len(emails)} emails.")