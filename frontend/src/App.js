import {Feature, Navbar} from './components';
import './App.css';
import React from 'react';
import axios from 'axios';
import "./components/assets/demand.png"


const App = () => {
  const [imagePath, setImagePath] = React.useState("");
  const [numPath, setNumber] = React.useState("");
//makes a request to the backend to run get_graph and update img_path
  const componentDidMount = () => {
// Make a GET request to a Flask API endpoint
    axios.get('http://127.0.0.1:5000/api/data')
      .then((response) => {
        setImagePath(response.data['img_path'])
        setNumber(response.data['dummy']);
//check developer tools to ensure that this message appears
        console.log("data fetched from backend");
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  }

  

  return (
    <div>
      <div className = "row">
        <div className ="navbar">
          <Navbar />
        </div>
        <div className='elements'>
          {/* <div style={{backgroundColor : 'blue', padding : 20, alignItems: 'center', width: 400, justifycontent: 'center', aligncontent: 'center'}}> */}
            <button onClick={componentDidMount}>
              <p>
                Update Graph
              </p>
            </button>
            {imagePath && <img src={require("./components/assets/demand.png")} alt="img" width ="300" justifycontent="center"/> }
          {/* </div> */}
          <Feature />
          <p>Dummy Value: {dummy}</p>
        </div>
      </div >
    </div>
  );
}
export default App;