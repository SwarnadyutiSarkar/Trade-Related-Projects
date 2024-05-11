// App.js
import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [shippingDocuments, setShippingDocuments] = useState([]);

  useEffect(() => {
    fetchShippingDocuments();
  }, []);

  const fetchShippingDocuments = async () => {
    try {
      const response = await fetch('http://localhost:5000/api/shipping_documents');
      const data = await response.json();
      setShippingDocuments(data);
    } catch (error) {
      console.error('Error fetching shipping documents:', error);
    }
  };

  return (
    <div className="App">
      <h1>Trade Compliance Management System</h1>
      <h2>Shipping Documents:</h2>
      <ul>
        {shippingDocuments.map(document => (
          <li key={document.id}>{document.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
