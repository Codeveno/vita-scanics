import React, { useState } from 'react';

const EmergencyAlerts = () => {
  const [alertMessage, setAlertMessage] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Alert Message:', alertMessage);
    // Send alert message to the backend
  };

  return (
    <div>
      <h2>Emergency Alerts</h2>
      <form onSubmit={handleSubmit}>
        <label>
          Alert Message:
          <textarea value={alertMessage} onChange={(e) => setAlertMessage(e.target.value)} />
        </label>
        <button type="submit">Send Alert</button>
      </form>
    </div>
  );
};

export default EmergencyAlerts;