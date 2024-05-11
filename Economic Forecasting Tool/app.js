// App.js
import React, { useState } from 'react';
import './App.css';

function App() {
  const [years, setYears] = useState('');
  const [values, setValues] = useState('');
  const [forecast, setForecast] = useState([]);

  const handleForecast = async () => {
    try {
      const response = await fetch('http://localhost:5000/api/forecast', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ years: years.split(',').map(year => parseInt(year)), values: values.split(',').map(value => parseInt(value)) })
      });
      const data = await response.json();
      setForecast(data.forecast);
    } catch (error) {
      console.error('Error forecasting:', error);
    }
  };

  return (
    <div className="App">
      <h1>Economic Forecasting Tool</h1>
      <div>
        <label>Years (comma-separated):</label>
        <input type="text" value={years} onChange={e => setYears(e.target.value)} />
      </div>
      <div>
        <label>Values (comma-separated):</label>
        <input type="text" value={values} onChange={e => setValues(e.target.value)} />
      </div>
      <button onClick={handleForecast}>Forecast</button>
      <div>
        <h2>Forecast:</h2>
        {forecast.length > 0 ? (
          <ul>
            {forecast.map((value, index) => (
              <li key={index}>{value}</li>
            ))}
          </ul>
        ) : (
          <p>No forecast available</p>
        )}
      </div>
    </div>
  );
}

export default App;
