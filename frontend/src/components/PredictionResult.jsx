export default function PredictionResult({ result }) {
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
}