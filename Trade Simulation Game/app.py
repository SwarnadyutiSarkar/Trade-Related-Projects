# app.py
from flask import Flask, request, jsonify, g
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

DATABASE = 'trade_simulation.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/api/start_game', methods=['POST'])
def start_game():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS players (id INTEGER PRIMARY KEY, name TEXT)')
    cursor.execute('DELETE FROM players')
    db.commit()
    data = request.json
    for player in data['players']:
        cursor.execute('INSERT INTO players (name) VALUES (?)', (player,))
    db.commit()
    return jsonify({'message': 'Game started successfully'})

@app.route('/api/players', methods=['GET'])
def get_players():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM players')
    players = cursor.fetchall()
    return jsonify([{'id': player[0], 'name': player[1]} for player in players])

if __name__ == '__main__':
    app.run(debug=True)
