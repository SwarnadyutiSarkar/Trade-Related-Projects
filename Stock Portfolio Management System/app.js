// App.js
import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [stocks, setStocks] = useState([]);
  const [symbol, setSymbol] = useState('');
  const [quantity, setQuantity] = useState('');

  useEffect(() => {
    fetchStocks();
  }, []);

  const fetchStocks = async () => {
    try {
      const response = await fetch('http://localhost:5000/api/stocks');
      const data = await response.json();
      setStocks(data);
    } catch (error) {
      console.error('Error fetching stocks:', error);
    }
  };

  const addStock = async () => {
    try {
      const response = await fetch('http://localhost:5000/api/stocks', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ symbol, quantity: parseInt(quantity) })
      });
      await response.json();
      fetchStocks();
      setSymbol('');
      setQuantity('');
    } catch (error) {
      console.error('Error adding stock:', error);
    }
  };

  return (
    <div className="App">
      <h1>Stock Portfolio Management System</h1>
      <div>
        <input type="text" placeholder="Symbol" value={symbol} onChange={e => setSymbol(e.target.value)} />
        <input type="number" placeholder="Quantity" value={quantity} onChange={e => setQuantity(e.target.value)} />
        <button onClick={addStock}>Add Stock</button>
      </div>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Symbol</th>
            <th>Quantity</th>
          </tr>
        </thead>
        <tbody>
          {stocks.map(stock => (
            <tr key={stock.id}>
              <td>{stock.id}</td>
              <td>{stock.symbol}</td>
              <td>{stock.quantity}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;
