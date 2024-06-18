import React, { useState, useEffect } from 'react';
import axios from 'axios';
import CryptoList from './components/CryptoList';

const App = () => {
  const [cryptos, setCryptos] = useState([]);

  useEffect(() => {
    const fetchCryptos = async () => {
      const response = await axios.get('http://localhost:8000/api/v1/crypto/');
      setCryptos(response.data);
    };
    fetchCryptos();
  }, []);

  return (
    <div className="App">
      <h1>Cryptocurrency Prices</h1>
      <CryptoList cryptos={cryptos} />
    </div>
  );
};

export default App;
