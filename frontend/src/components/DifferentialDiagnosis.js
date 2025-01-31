import React, { useState } from 'react';

const DifferentialDiagnosis = () => {
  const [symptoms, setSymptoms] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Symptoms:', symptoms);
    // Send symptoms to the backend for analysis
  };

  return (
    <div>
      <h2>Differential Diagnosis</h2>
      <form onSubmit={handleSubmit}>
        <label>
          Symptoms:
          <textarea value={symptoms} onChange={(e) => setSymptoms(e.target.value)} />
        </label>
        <button type="submit">Analyze</button>
      </form>
    </div>
  );
};

export default DifferentialDiagnosis;