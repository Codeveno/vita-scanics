import React, { useState } from 'react';

const ClinicalTrials = () => {
  const [trialName, setTrialName] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Trial Name:', trialName);
    // Send trial name to the backend for analysis
  };

  return (
    <div>
      <h2>Clinical Trials</h2>
      <form onSubmit={handleSubmit}>
        <label>
          Trial Name:
          <input type="text" value={trialName} onChange={(e) => setTrialName(e.target.value)} />
        </label>
        <button type="submit">Search</button>
      </form>
    </div>
  );
};

export default ClinicalTrials;