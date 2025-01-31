import React from 'react';
import Dashboard from '../components/Dashboard';
import './styles/global.css';

const Home = () => {
  return (
    <div className="container">
      <h1>Welcome to Vita-Scanics</h1>
      <Dashboard />
    </div>
  );
};

export default Home;