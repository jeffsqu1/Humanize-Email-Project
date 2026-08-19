from fastapi import FastAPI
import requests
from retrieve import retrieve_similar, build_prompt

app = FastAPI()

@app.post("/humanize")
def humanize(payload: dict):
    draft = payload["draft"]
    tone = payload.get("tone", "professional")
    model = payload.get("model", "llama3.2")

    examples = retrieve_similar(draft)
    prompt = build_prompt(draft, examples, tone)

    resp = requests.post("http://localhost:11434/api/generate", json={
        "model": model,
        "prompt": prompt,
        "stream": False
    })
    output = resp.json()["response"]

    return {"result": output, "used_examples": len(examples)}