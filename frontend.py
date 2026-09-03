import os

files = {
"frontend/package.json": """{
  "name": "financial-fraud-frontend",
  "private": true,
  "version": "1.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  },
  "devDependencies": {
    "@vitejs/plugin-react": "^4.2.1",
    "vite": "^5.2.0"
  }
}""",

"frontend/index.html": """<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <title>Financial Fraud Detection System</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>""",

"frontend/vite.config.js": """import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
})""",

"frontend/src/main.jsx": """import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './styles.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)""",

"frontend/src/styles.css": """:root {
  --bg-color: #0d1117;
  --card-bg: #161b22;
  --text-main: #e6edf3;
  --text-muted: #8b949e;
  --accent-blue: #2f81f7;
  --accent-blue-hover: #1f6feb;
  --fraud-color: #f85149;
  --legit-color: #238636;
  --border-color: #30363d;
  --input-bg: #0d1117;
  --font-family: 'Inter', sans-serif;
}

* { box-sizing: border-box; margin: 0; padding: 0; }
body { background-color: var(--bg-color); color: var(--text-main); font-family: var(--font-family); line-height: 1.5; -webkit-font-smoothing: antialiased; }
.app-container { max-width: 1200px; margin: 0 auto; padding: 2rem; }
.header { text-align: center; margin-bottom: 3rem; }
.header h1 { font-size: 2rem; font-weight: 700; margin-bottom: 0.5rem; }
.header p { color: var(--text-muted); font-size: 1.1rem; }
.main-content { display: grid; grid-template-columns: 2fr 1fr; gap: 2rem; }
@media (max-width: 900px) { .main-content { grid-template-columns: 1fr; } }
.card { background-color: var(--card-bg); border: 1px solid var(--border-color); border-radius: 8px; padding: 1.5rem; margin-bottom: 1.5rem; }
.card h2 { font-size: 1.25rem; margin-bottom: 1rem; border-bottom: 1px solid var(--border-color); padding-bottom: 0.5rem; }
.form-group { margin-bottom: 1rem; }
.form-group label { display: block; font-size: 0.85rem; font-weight: 500; margin-bottom: 0.25rem; color: var(--text-muted); }
.form-group input { width: 100%; padding: 0.5rem; background-color: var(--input-bg); border: 1px solid var(--border-color); color: var(--text-main); border-radius: 4px; font-family: inherit; }
.form-group input:focus { outline: none; border-color: var(--accent-blue); }
.primary-inputs { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-bottom: 1.5rem; }
.pca-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(120px, 1fr)); gap: 0.75rem; }
.button-group { display: flex; gap: 1rem; margin-top: 2rem; flex-wrap: wrap; }
button { padding: 0.75rem 1.5rem; border: none; border-radius: 6px; font-weight: 600; cursor: pointer; font-family: inherit; transition: opacity 0.2s, background-color 0.2s; }
button:disabled { opacity: 0.5; cursor: not-allowed; }
.btn-primary { background-color: var(--accent-blue); color: white; flex: 1; }
.btn-primary:hover:not(:disabled) { background-color: var(--accent-blue-hover); }
.btn-secondary { background-color: transparent; color: var(--text-main); border: 1px solid var(--border-color); }
.btn-secondary:hover:not(:disabled) { background-color: var(--border-color); }
.error-banner { background-color: rgba(248, 81, 73, 0.1); border: 1px solid var(--fraud-color); color: #ff7b72; padding: 1rem; border-radius: 6px; margin-bottom: 1.5rem; }
.result-box { text-align: center; padding: 2rem 1rem; border-radius: 6px; margin-top: 1rem; }
.result-box.fraud { background-color: rgba(248, 81, 73, 0.1); border: 1px solid var(--fraud-color); }
.result-box.legitimate { background-color: rgba(35, 134, 54, 0.1); border: 1px solid var(--legit-color); }
.result-title { font-size: 1.5rem; font-weight: 700; margin-bottom: 0.5rem; }
.fraud .result-title { color: var(--fraud-color); }
.legitimate .result-title { color: var(--legit-color); }
.result-prob { font-size: 1rem; color: var(--text-muted); }
.disclaimer { font-size: 0.8rem; color: var(--text-muted); text-align: center; margin-top: 3rem; padding-top: 1rem; border-top: 1px solid var(--border-color); }""",

"frontend/src/services/api.js": """const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || "http://127.0.0.1:8000";

export const predictTransaction = async (transactionData) => {
  try {
    const response = await fetch(`${API_BASE_URL}/predict`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(transactionData),
    });
    if (!response.ok) {
      if (response.status === 422) throw new Error("Validation Error: Please check that all 30 inputs are valid numbers.");
      if (response.status === 500) throw new Error("Backend Error: The ML model encountered an error.");
      throw new Error(`Error: Received status code ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    if (error.name === 'TypeError' && error.message === 'Failed to fetch') {
      throw new Error("Network Error: Cannot connect to backend. Ensure FastAPI is running and CORS is configured.");
    }
    throw error;
  }
};""",

"frontend/src/components/TransactionForm.jsx": """import { useState } from 'react';

const V_FEATURES = Array.from({ length: 28 }, (_, i) => `V${i + 1}`);
const SAMPLE_DATA = { "Time": 79486.0, "V1": 0.8104590607978, "V2": -0.449732294677454, "V3": 0.761882256152219, "V4": 1.22386582272629, "V5": -0.599513764568542, "V6": 0.405457862810437, "V7": -0.258305659308653, "V8": 0.184438375315336, "V9": 0.224597592350399, "V10": -0.0771594856767156, "V11": 1.34149342409989, "V12": 1.46156443357907, "V13": 0.596549068668564, "V14": 0.0102929038087334, "V15": -0.0433393798644203, "V16": -0.0546261397102752, "V17": -0.326212867137541, "V18": 0.0695047692928731, "V19": -0.473855755150496, "V20": 0.189960198450105, "V21": 0.297067171355441, "V22": 0.723396025002655, "V23": -0.257987760135181, "V24": 0.0672617933152718, "V25": 0.501125381754329, "V26": -0.229681630565959, "V27": 0.0410479391964013, "V28": 0.0432974935342779, "Amount": 158.0 };

const getEmptyState = () => { const state = { Time: '', Amount: '' }; V_FEATURES.forEach(v => state[v] = ''); return state; };

export default function TransactionForm({ onSubmit, isLoading, onReset }) {
  const [formData, setFormData] = useState(getEmptyState());
  const [localError, setLocalError] = useState(null);

  const handleChange = (e) => setFormData(prev => ({ ...prev, [e.target.name]: e.target.value }));
  const handleLoadSample = () => { setFormData(SAMPLE_DATA); setLocalError(null); };
  const handleReset = () => { setFormData(getEmptyState()); setLocalError(null); onReset(); };

  const handleSubmit = (e) => {
    e.preventDefault();
    setLocalError(null);
    const payload = {};
    for (const key in formData) {
      if (formData[key] === '' || formData[key] === null) return setLocalError(`Missing field: ${key}`);
      const numVal = Number(formData[key]);
      if (isNaN(numVal)) return setLocalError(`Invalid number in field: ${key}`);
      payload[key] = numVal;
    }
    onSubmit(payload);
  };

  return (
    <div className="card">
      <h2>Transaction Details</h2>
      {localError && <div className="error-banner">{localError}</div>}
      <form onSubmit={handleSubmit}>
        <div className="primary-inputs">
          <div className="form-group"><label>Time</label><input type="number" step="any" name="Time" value={formData.Time} onChange={handleChange} /></div>
          <div className="form-group"><label>Amount ($)</label><input type="number" step="any" name="Amount" value={formData.Amount} onChange={handleChange} /></div>
        </div>
        <h3 style={{ fontSize: '1rem', marginBottom: '1rem', color: 'var(--text-muted)' }}>PCA Features (V1 - V28)</h3>
        <div className="pca-grid">
          {V_FEATURES.map(v => (
            <div className="form-group" key={v}><label>{v}</label><input type="number" step="any" name={v} value={formData[v]} onChange={handleChange} /></div>
          ))}
        </div>
        <div className="button-group">
          <button type="submit" className="btn-primary" disabled={isLoading}>{isLoading ? 'Analyzing...' : 'Analyze Transaction'}</button>
          <button type="button" className="btn-secondary" onClick={handleLoadSample} disabled={isLoading}>Load Sample</button>
          <button type="button" className="btn-secondary" onClick={handleReset} disabled={isLoading}>Reset</button>
        </div>
      </form>
    </div>
  );
}""",

"frontend/src/components/PredictionResult.jsx": """export default function PredictionResult({ result }) {
  if (!result) return null;
  const isFraud = result.label === "FRAUD";
  const percentage = (result.fraud_probability * 100).toFixed(4);

  return (
    <div className="card">
      <h2>Analysis Result</h2>
      <div className={`result-box ${isFraud ? 'fraud' : 'legitimate'}`}>
        <div className="result-title">{isFraud ? "🚨 FRAUD DETECTED" : "✅ LEGITIMATE"}</div>
        <div className="result-prob">Fraud Probability: <strong>{percentage}%</strong></div>
        <div style={{ marginTop: '0.5rem', fontSize: '0.85rem', color: 'var(--text-muted)' }}>Raw Prediction: {result.prediction}</div>
      </div>
    </div>
  );
}""",

"frontend/src/components/ModelInfo.jsx": """export default function ModelInfo() {
  return (
    <>
      <div className="card">
        <h2>Model Explainability</h2>
        <p style={{ color: 'var(--text-muted)', fontSize: '0.9rem' }}>This fraud detection model uses SHAP explainability. Detailed transaction-level explanations can be integrated through the backend.</p>
      </div>
      <div className="card">
        <h2>About the Model</h2>
        <ul style={{ color: 'var(--text-muted)', fontSize: '0.9rem', paddingLeft: '1.2rem', lineHeight: '1.8' }}>
          <li><strong>Architecture:</strong> XGBoost Binary Classifier</li>
          <li><strong>Decision Threshold:</strong> 0.20</li>
          <li><strong>Dataset:</strong> Kaggle Credit Card Fraud</li>
          <li><strong>Features:</strong> Time, Amount, V1-V28</li>
        </ul>
      </div>
    </>
  );
}""",

"frontend/src/App.jsx": """import { useState } from 'react';
import TransactionForm from './components/TransactionForm';
import PredictionResult from './components/PredictionResult';
import ModelInfo from './components/ModelInfo';
import { predictTransaction } from './services/api';

export default function App() {
  const [result, setResult] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [apiError, setApiError] = useState(null);

  const handlePredict = async (payload) => {
    setIsLoading(true); setApiError(null); setResult(null);
    try { setResult(await predictTransaction(payload)); } 
    catch (err) { setApiError(err.message); } 
    finally { setIsLoading(false); }
  };

  return (
    <div className="app-container">
      <header className="header">
        <h1>Financial Fraud Detection System</h1>
        <p>XGBoost-powered transaction risk analysis</p>
      </header>
      <main className="main-content">
        <section className="form-section"><TransactionForm onSubmit={handlePredict} isLoading={isLoading} onReset={() => {setResult(null); setApiError(null);}} /></section>
        <aside className="sidebar">
          {apiError && <div className="error-banner">{apiError}</div>}
          <PredictionResult result={result} />
          <ModelInfo />
        </aside>
      </main>
      <footer className="disclaimer">For educational and portfolio purposes only.</footer>
    </div>
  );
}"""
}

# Create folders and write files
for file_path, content in files.items():
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content.strip())

print("✅ Boom! All React files created successfully in the 'frontend' folder.")
print("👉 Next steps:")
print("1. cd frontend")
print("2. npm install")
print("3. npm run dev")