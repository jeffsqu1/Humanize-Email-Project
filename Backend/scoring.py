import json
import os
from datetime import datetime

LOG_PATH = "preference_log.jsonl"

def score_output(draft: str, output: str) -> float:
    if not output.strip():
        return 0.0
    length_ratio = len(output) / max(len(draft), 1)
    if length_ratio < 0.4 or length_ratio > 2.5:
        return 0.3
    contractions = sum(output.count(c) for c in ["'re", "'ve", "'ll", "n't", "'m"])
    # Don't require contractions to pass — reward them, don't gate on them
    return min(1.0, 0.7 + contractions * 0.1)

def log_preference(draft: str, examples: list[str], output: str, score: float, attempt: int):
    record = {
        "timestamp": datetime.utcnow().isoformat(),
        "draft": draft,
        "retrieved_examples": examples,
        "output": output,
        "score": score,
        "attempt": attempt,
    }
    with open(LOG_PATH, "a") as f:
        f.write(json.dumps(record) + "\n")