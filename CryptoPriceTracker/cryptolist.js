import React from 'react';
import CryptoItem from './CryptoItem';

const CryptoList = ({ cryptos }) => {
  return (
    <div className="crypto-list">
      {cryptos.map(crypto => (
        <CryptoItem key={crypto.id} crypto={crypto} />
      ))}
    </div>
  );
};

export default CryptoList;
