import React, { useState } from 'react';

const PredictionForm = () => {
  const [feature1, setFeature1] = useState('');
  const [feature2, setFeature2] = useState('');
  const [feature3, setFeature3] = useState('');
  const [prediction, setPrediction] = useState(null);

  const handlePrediction = async () => {
    try{

    
      const response = await fetch('http://localhost:5000/api/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          features: [parseFloat(feature1), parseFloat(feature2), parseFloat(feature3)],
        }),
      });

      if (response.ok) {
        const result = await response.json();
        setPrediction(result.prediction);
      } else {
        console.error('Failed to make prediction:', response.status);
      }
    } catch (error) {
      console.error('Error in handlePrediction:', error);
    } 
  };

  return (
    <div>
      <h2>Charge Rate Prediction</h2>
      <label>
        Timestamp:
        <input type="text" value={feature1} onChange={(e) => setFeature1(e.target.value)} />
      </label>
      <label>
        Price:
        <input type="text" value={feature2} onChange={(e) => setFeature2(e.target.value)} />
      </label>
      <label>
        Demand:
        <input type="text" value={feature3} onChange={(e) => setFeature3(e.target.value)} />
      </label>
      <button onClick={handlePrediction}>Predict</button>
      {prediction !== null && <p>Prediction: {prediction}</p>}
    </div>
  );
};

export default PredictionForm;
