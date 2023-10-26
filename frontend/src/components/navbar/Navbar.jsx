import React from 'react';
import './navbar.css';
// import home from "frontend/src/components/assets/Home.png";
// import logo from "frontend/src/components/assets/logo.png";

function Navbar() {
  return (
  <div className= "sidenav">
    <div className= ".logo">
      {/* <img src = {logo} alt="badbadbad"/> */}
    </div>
      <div className = "block"> 
        <div>
          {/* <img src={home} alt="this is very bad"/> */}
          hello
        </div>
        <div>
          what
        </div>
      </div>
  </div>
   );
};
  
  export default Navbar;