import { useState } from "react";

type Health = { status: string; app: string; version: string };

export default function App() {
  const [health, setHealth] = useState<Health | null>(null);
  const [error, setError] = useState("");

  async function testApi() {
    setError("");
    try {
      const response = await fetch("http://127.0.0.1:8000/health");
      if (!response.ok) throw new Error(`API returned ${response.status}`);
      setHealth(await response.json());
    } catch (err) {
      setHealth(null);
      setError(err instanceof Error ? err.message : "Unable to reach API");
    }
  }

  return (
    <main className="shell">
      <aside className="sidebar">
        <div className="brand">HYPERPIX</div>
        <nav>
          <button className="active">Enhance</button>
          <button>Restore</button>
          <button>Portrait</button>
          <button>Depth</button>
          <button>Export</button>
        </nav>
      </aside>

      <section className="workspace">
        <header>
          <div>
            <p className="eyebrow">AI IMAGE LAB</p>
            <h1>Push every pixel further.</h1>
          </div>
          <button className="primary" onClick={testApi}>Test AI Engine</button>
        </header>

        <div className="viewer">
          <div className="dropzone">
            <strong>Drop an image here</strong>
            <span>HYPERPIX v0.1 infrastructure is online.</span>
          </div>
        </div>

        <footer>
          {health && <span>API: {health.status} · {health.app} {health.version}</span>}
          {error && <span className="error">API offline: {error}</span>}
        </footer>
      </section>

      <aside className="inspector">
        <p className="eyebrow">AI ANALYSIS</p>
        <div className="metric"><span>Resolution</span><b>—</b></div>
        <div className="metric"><span>Noise</span><b>—</b></div>
        <div className="metric"><span>Blur</span><b>—</b></div>
        <div className="metric"><span>Faces</span><b>—</b></div>
        <hr />
        <p className="muted">Import and analyze an image to populate these metrics.</p>
      </aside>
    </main>
  );
}
