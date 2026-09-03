export default function ModelInfo() {
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
}