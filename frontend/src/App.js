import React from 'react';


import {Feature, Navbar} from './components';

import './App.css';

const App = () => (
  <div className = "row">
    <div class="navbar">
      <Navbar />
    </div>
    <div class = "elements">
      <Feature />
    </div>
  </div>
  );

export default App;
