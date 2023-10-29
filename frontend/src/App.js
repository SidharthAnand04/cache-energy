import {Feature, Navbar} from './components';
import './App.css';
import React from 'react';
import axios from 'axios';

const App = () => {
  const [data, setData] = React.useState(null);

  const componentDidMount = () => {
    // Make a GET request to a Flask API endpoint
    axios.get('http://127.0.0.1:5000/api/data')
      .then((response) => {
        console.log(response);
        setData(response.data)
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
        <div className = "elements">
          <div style={{backgroundColor : 'blue', padding : 20, alignItems: 'center'}}>
          <button onClick={componentDidMount}>
            <p>
              press me!
              {JSON.stringify(data)};
            </p>
          </button>
        </div>
          <Feature />
        </div>
      </div >
    </div>
  );
}

// class App extends Component {
//   constructor() {
//     super();
//     this.state = {
//       responseData: null, // Initialize responseData in the component's state
//     };
//   }

//   componentDidMount() {
//     // Make a GET request to a Flask API endpoint
//     axios.get('http://127.0.0.1:5000/api/data')
//       .then((response) => {
//         console.log(response);
//         this.setState({ responseData: response.data }); // Set the response data in state
//         console.log("data fetched from backend");
//       })
//       .catch((error) => {
//         console.error('Error:', error);
//       });
//   }

//   render() {
//     return (
//       <div>
//         <div className = "row">
//           <div className ="navbar">
//             <Navbar />
//           </div>
//           <div className = "elements">
//             <div style={{backgroundColor : 'blue', padding : 20, alignItems: 'center'}}>
//             <button onClick={this.componentDidMount}>
//               <p>
//                 press me!
//                 {this.responseData}
//               </p>
//             </button>
//           </div>
//             <Feature />
//           </div>
//         </div >
//       </div>
//     );
//   }
// }
export default App;


