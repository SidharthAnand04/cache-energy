import React from 'react';
import './navbar.css';
import logo from '/Users/eduar/Desktop/cacheenergy/cache-energy/frontend/src/components/assets/logo.png';

function Navbar() {
  return (
  <div className= "sidenav">
    <div className= ".logo">
      <img src = {logo} alt="badbadbad" width = '110'/>
    </div>
      <div className = "block"> 
        <div>
          Home
        </div>
      </div>
  </div>
   );
};
  
  export default Navbar;