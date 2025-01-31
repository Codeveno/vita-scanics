import React from 'react';
import './styles/components.css';

const Dashboard = () => {
  return (
    <div className="dashboard">
      <h1>Dashboard</h1>
      <div className="grid">
        <div className="differential-diagnosis">
          <h2>Differential Diagnosis</h2>
          <p>Analyze symptoms and predict conditions.</p>
        </div>
        <div className="predictive-health">
          <h2>Predictive Health</h2>
          <p>Assess health risks and early disease detection.</p>
        </div>
        <div className="mental-health">
          <h2>Mental Health</h2>
          <p>Analyze behavioral patterns and mental health conditions.</p>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;