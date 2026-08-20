from embedding import embed
from ingest import collection

def retrieve_similar(draft: str, k: int = 3) -> list[str]:
    query_embedding = embed(draft)
    results = collection.query(query_embeddings=[query_embedding], n_results=k)
    return results["documents"][0]

def build_prompt(draft: str, examples: list[str], tone: str = "professional") -> str:
    examples_block = "\n\n".join(f"Example {i+1}:\n{ex}" for i, ex in enumerate(examples))
    return f"""You rewrite emails to sound natural and human, in a {tone} tone.
Study the writing patterns below — sentence rhythm, contractions, directness — and apply the same voice to the draft.

{examples_block}

Draft to rewrite:
{draft}

Output ONLY the rewritten email between the tags below. No preamble, no meta-commentary, no explanation of what you're doing — just the email itself.

<email>
[rewritten email goes here]
</email>"""