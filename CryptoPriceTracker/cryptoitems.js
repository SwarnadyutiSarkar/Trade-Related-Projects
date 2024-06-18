import React from 'react';

const CryptoItem = ({ crypto }) => {
  return (
    <div className="crypto-item">
      <h2>{crypto.name}</h2>
      <p>Current Price: ${crypto.current_price}</p>
      <p>Market Cap: ${crypto.market_cap}</p>
      <p>24h Change: {crypto.price_change_percentage_24h}%</p>
    </div>
  );
};

export default CryptoItem;
