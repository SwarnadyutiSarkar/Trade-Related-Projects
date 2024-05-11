// App.js
import React, { useState } from 'react';
import './App.css';

function App() {
  const [demand, setDemand] = useState('');
  const [supply, setSupply] = useState('');
  const [costs, setCosts] = useState('');
  const [result, setResult] = useState({});

  const handleOptimize = async () => {
    try {
      const response = await fetch('http://localhost:5000/api/optimize', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ demand: demand, supply: supply, costs: costs })
      });
      const data = await response.json();
      setResult(data);
    } catch (error) {
      console.error('Error optimizing supply chain:', error);
    }
  };

  return (
    <div className="App">
      <h1>Supply Chain Optimization Software</h1>
      <div>
        <label>Demand:</label>
        <input type="text" value={demand} onChange={e => setDemand(e.target.value)} />
      </div>
      <div>
        <label>Supply:</label>
        <input type="text" value={supply} onChange={e => setSupply(e.target.value)} />
      </div>
      <div>
        <label>Costs:</label>
        <input type="text" value={costs} onChange={e => setCosts(e.target.value)} />
      </div>
      <button onClick={handleOptimize}>Optimize</button>
      <h2>Optimized Solution:</h2>
      <ul>
        {Object.keys(result).map((key, index) => (
          <li key={index}>{key}: {result[key]}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
