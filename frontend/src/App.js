import React from 'react';
import { Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import Diagnosis from './pages/Diagnosis';
import Recommendations from './pages/Recommendations';
import TelemedicineSession from './pages/TelemedicineSession';
import './styles/global.css';

const App = () => {
  return (
    <div className="app">
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/diagnosis" element={<Diagnosis />} />
        <Route path="/recommendations" element={<Recommendations />} />
        <Route path="/telemedicine" element={<TelemedicineSession />} />
      </Routes>
    </div>
  ); 
};

export default App;
