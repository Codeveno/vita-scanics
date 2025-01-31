import React from 'react';
import { Link } from 'react-router-dom';
import './styles/components.css';

const Navbar = () => {
  return (
    <nav className="navbar">
      <Link to="/" className="nav-link">Home</Link>
      <Link to="/diagnosis" className="nav-link">Diagnosis</Link>
      <Link to="/recommendations" className="nav-link">Recommendations</Link>
      <Link to="/telemedicine" className="nav-link">Telemedicine</Link>
    </nav>
  );
};

export default Navbar;