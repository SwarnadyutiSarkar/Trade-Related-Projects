// App.js
import React, { useState } from 'react';
import './App.css';

function App() {
  const [players, setPlayers] = useState([]);
  const [playerName, setPlayerName] = useState('');

  const handleStartGame = async () => {
    try {
      const response = await fetch('http://localhost:5000/api/start_game', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ players: players })
      });
      await response.json();
      fetchPlayers();
    } catch (error) {
      console.error('Error starting game:', error);
    }
  };

  const fetchPlayers = async () => {
    try {
      const response = await fetch('http://localhost:5000/api/players');
      const data = await response.json();
      setPlayers(data);
    } catch (error) {
      console.error('Error fetching players:', error);
    }
  };

  return (
    <div className="App">
      <h1>Trade Simulation Game</h1>
      <div>
        <input type="text" placeholder="Player Name" value={playerName} onChange={e => setPlayerName(e.target.value)} />
        <button onClick={() => setPlayers([...players, playerName])}>Add Player</button>
      </div>
      <button onClick={handleStartGame}>Start Game</button>
      <h2>Players:</h2>
      <ul>
        {players.map(player => (
          <li key={player.id}>{player.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
