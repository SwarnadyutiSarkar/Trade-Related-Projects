// App.js
import React, { useState } from 'react';
import './App.css';

function App() {
  const [text, setText] = useState('');
  const [sentiment, setSentiment] = useState(null);

  const handleAnalyzeSentiment = async () => {
    try {
      const response = await fetch('http://localhost:5000/api/sentiment', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: text })
      });
      const data = await response.json();
      setSentiment(data.sentiment);
    } catch (error) {
      console.error('Error analyzing sentiment:', error);
    }
  };

  return (
    <div className="App">
      <h1>Market Sentiment Analysis Tool</h1>
      <div>
        <textarea rows="5" cols="50" value={text} onChange={e => setText(e.target.value)}></textarea>
      </div>
      <button onClick={handleAnalyzeSentiment}>Analyze Sentiment</button>
      {sentiment !== null && (
        <div>
          <h2>Sentiment Score:</h2>
          <p>{sentiment}</p>
        </div>
      )}
    </div>
  );
}

export default App;
