import { useState } from 'react';

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
}