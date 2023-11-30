import React from 'react';
import './navbar.css';
import logo from "./logo.png";
import home from "./Home.png";


function Navbar() {
  return (
  <div className= "sidenav">
    <div >
      {
      <img src={logo} alt="top left corner logo"
      />
      }
    </div>
    <div className = "block">
      <div>
        <img src={home} alt="home thing" className="image"/>
          Home
        </div>
      <div>
          Energy
        </div>
        <div>
          Finance
        </div>
      </div>
  </div>
   );
};
  export default Navbar;

