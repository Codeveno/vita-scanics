import React, { useState } from 'react';

const MentalHealth = () => {
  const [behavioralPatterns, setBehavioralPatterns] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Behavioral Patterns:', behavioralPatterns);
    // Send behavioral patterns to the backend for analysis
  };

  return (
    <div>
      <h2>Mental Health Analysis</h2>
      <form onSubmit={handleSubmit}>
        <label>
          Behavioral Patterns:
          <textarea value={behavioralPatterns} onChange={(e) => setBehavioralPatterns(e.target.value)} />
        </label>
        <button type="submit">Analyze</button>
      </form>
    </div>
  );
};

export default MentalHealth;