const API_BASE = "http://localhost:8000";

export async function humanizeEmail(draft, tone, model = "llama3.2") {
  const res = await fetch(`${API_BASE}/humanize`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ draft, tone, model }),
  });
  if (!res.ok) {
    throw new Error(`Request failed: ${res.status}`);
  }
  return res.json();
}