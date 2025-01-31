import React, { useState } from 'react';

const PredictiveHealth = () => {
  const [riskFactors, setRiskFactors] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Risk Factors:', riskFactors);
    // Send risk factors to the backend for analysis
  };

  return (
    <div>
      <h2>Predictive Health</h2>
      <form onSubmit={handleSubmit}>
        <label>
          Risk Factors:
          <textarea value={riskFactors} onChange={(e) => setRiskFactors(e.target.value)} />
        </label>
        <button type="submit">Analyze</button>
      </form>
    </div>
  );
};

export default PredictiveHealth;