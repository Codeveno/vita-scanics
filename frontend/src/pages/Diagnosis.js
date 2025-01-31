import React from 'react';
import DifferentialDiagnosis from '../components/DifferentialDiagnosis';
import './styles/global.css';

const Diagnosis = () => {
  return (
    <div className="container">
      <h1>Diagnosis</h1>
      <DifferentialDiagnosis />
    </div>
  );
};

export default Diagnosis;