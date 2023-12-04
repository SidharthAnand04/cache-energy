import {Feature, Navbar, PaperCard} from './components';
import './App.css';
import React from 'react';
import axios from 'axios';
//import "./components/assets/demand.png"



//papercard stuff
import './components/papercard/paper.css';
import Paper from '@mui/material/Paper';
import Container from '@mui/material/Container';
import Grid from '@mui/material/Grid';


const App = () => {
  // const [imagePath, setImagePath] = React.useState("");
  // const [fig1Path, setfig1Path] = React.useState("")
  // const [fig2Path, setfig2Path] = React.useState("")
  // const [fig3Path, setfig3Path] = React.useState("")
  // const [fig4Path, setfig4Path] = React.useState("")
  // const [figTvEPath, setfigTvEPath] = React.useState("")
  
//makes a request to the backend to run get_graph and update img_path
  const componentDidMount = () => {
    
// Make a GET request to a Flask API endpoint
    axios.get('http://127.0.0.1:5000/api/data')
      .then((response) => {
        
        // setImagePath(response.data['img_path'])
        // setfig1Path(response.data['fig1_path'])
        // setfig2Path(response.data['fig2_path'])
        // setfig3Path(response.data['fig3_path'])
        // setfig4Path(response.data['fig4_path'])
        // setfigTvEPath(response.data['figTvE_path'])
        
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
            <button onClick={componentDidMount}>
              <p>
                Update Graphs
              </p>
            </button>
       
          <div className="cards">
            <Grid
              sx={{
                display: 'flex',
                flexWrap: 'wrap',
                '& > :not(style)': {
                  m: 5,
                  width: 400,
                  height: 300,
                },
              }}
            >
              <Paper elevation={3} 
                component='img'
                height='140px'
                img src={require("./components/assets/demand.png")}
              />
              <Paper elevation={3} 
                component='img'
                height='140px'
                img src={require("./components/assets/figTvE.png")}/>
              <Paper elevation={3} 
                component='img'
                height='140px'
                img src={require("./components/assets/fig1.png")}/>
              <Paper elevation={3} 
                component='img'
                height='140px'
                img src={require("./components/assets/fig2.png")}/>
              <Paper elevation={3} 
                component='img'
                height='140px'
                img src={require("./components/assets/fig3.png")}/>
              <Paper elevation={3} 
                component='img'
                height='140px'
                img src={require("./components/assets/fig4.png")}/>
            </Grid>
          </div>
        </div>
      </div >
    </div>
  );
}
export default App;