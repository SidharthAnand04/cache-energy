import React from 'react'
import './paper.css';
import Paper from '@mui/material/Paper';
import Container from '@mui/material/Container';
import Grid from '@mui/material/Grid';


function PaperCard(yay){
return (
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
        image src={yay}
      />
      <Paper elevation={3} />
      <Paper elevation={3} />
      <Paper elevation={3} />
    </Grid>
    </div>
    );
};
export default PaperCard;