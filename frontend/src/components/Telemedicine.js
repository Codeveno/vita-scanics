import React, { useState } from 'react';

const Telemedicine = () => {
  const [sessionDetails, setSessionDetails] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Session Details:', sessionDetails);
    // Send session details to the backend
  };

  return (
    <div>
      <h2>Telemedicine</h2>
      <form onSubmit={handleSubmit}>
        <label>
          Session Details:
          <textarea value={sessionDetails} onChange={(e) => setSessionDetails(e.target.value)} />
        </label>
        <button type="submit">Start Session</button>
      </form>
    </div>
  );
};

export default Telemedicine;