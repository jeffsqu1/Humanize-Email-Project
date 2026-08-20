import { useState } from "react";
import { humanizeEmail } from "./api";
import "./App.css";

const TONES = ["Casual", "Professional", "Formal", "Apologetic"];

function App() {
  const [draft, setDraft] = useState("");
  const [tone, setTone] = useState("professional");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async () => {
    if (!draft.trim()) return;
    setLoading(true);
    setError(null);
    setResult(null);
    try {
      const data = await humanizeEmail(draft, tone);
      setResult(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <h1>Email Humanizer</h1>

      <textarea
        value={draft}
        onChange={(e) => setDraft(e.target.value)}
        placeholder="Paste your draft email here..."
        rows={6}
      />

      <div className="controls">
        <select value={tone} onChange={(e) => setTone(e.target.value)}>
          {TONES.map((t) => (
            <option key={t} value={t}>{t}</option>
          ))}
        </select>
        <button onClick={handleSubmit} disabled={loading || !draft.trim()}>
          {loading ? "Humanizing..." : "Humanize"}
        </button>
      </div>

      {error && <p className="error">Error: {error}</p>}

      {result && (
        <div className="result">
          <h2>Result</h2>
          <p>{result.result}</p>
          <small>
            Score: {result.score?.toFixed(2) ?? "n/a"} · {result.used_examples} examples used
          </small>
        </div>
      )}
    </div>
  );
}

export default App;