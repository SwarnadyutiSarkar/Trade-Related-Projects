// App.js
import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [tradeData, setTradeData] = useState([]);

  useEffect(() => {
    fetchTradeData();
  }, []);

  const fetchTradeData = async () => {
    try {
      const response = await fetch('http://localhost:5000/api/trade_data');
      const data = await response.json();
      setTradeData(data);
    } catch (error) {
      console.error('Error fetching trade data:', error);
    }
  };

  return (
    <div className="App">
      <h1>Global Trade Analytics Platform</h1>
      <table>
        <thead>
          <tr>
            <th>Country</th>
            <th>Export Value</th>
            <th>Import Value</th>
          </tr>
        </thead>
        <tbody>
          {tradeData.map((item, index) => (
            <tr key={index}>
              <td>{item.country}</td>
              <td>{item.export_value}</td>
              <td>{item.import_value}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;
