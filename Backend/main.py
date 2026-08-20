from fastapi import FastAPI
import requests
from retrieve import retrieve_similar, build_prompt
from scoring import score_output, log_preference

app = FastAPI()

SCORE_THRESHOLD = 0.6
MAX_ATTEMPTS = 3

@app.post("/humanize")
def humanize(payload: dict):
    draft = payload["draft"]
    tone = payload.get("tone", "professional")
    model = payload.get("model", "llama3.2")

    examples = retrieve_similar(draft)
    best_output, best_score = None, -1.0

    for attempt in range(1, MAX_ATTEMPTS + 1):
        prompt = build_prompt(draft, examples, tone)
        resp = requests.post("http://localhost:11434/api/generate", json={
            "model": model,
            "prompt": prompt,
            "stream": False
        })
        output = resp.json()["response"]
        score = score_output(draft, output)
        log_preference(draft, examples, output, score, attempt)

        if score > best_score:
            best_output, best_score = output, score
        if score >= SCORE_THRESHOLD:
            break

    return {"result": best_output, "score": best_score, "used_examples": len(examples)}