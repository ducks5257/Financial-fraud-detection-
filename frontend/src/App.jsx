import { useState } from 'react';
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
}