// App.js
import React, { useState, useEffect } from 'react';
import './App.css';
import Plot from 'react-plotly.js';

function App() {
  const [financialData, setFinancialData] = useState(null);

  useEffect(() => {
    fetchFinancialData();
  }, []);

  const fetchFinancialData = async () => {
    try {
      const response = await fetch('http://localhost:5000/api/data');
      const data = await response.json();
      setFinancialData(data);
    } catch (error) {
      console.error('Error fetching financial data:', error);
    }
  };

  return (
    <div className="App">
      <h1>Financial Data Visualization Dashboard</h1>
      {financialData && (
        <div>
          <Plot
            data={financialData.data}
            layout={financialData.layout}
          />
        </div>
      )}
    </div>
  );
}

export default App;
