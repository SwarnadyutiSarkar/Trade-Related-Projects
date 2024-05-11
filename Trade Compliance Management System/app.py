# app.py
from flask import Flask, request, jsonify, g
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

DATABASE = 'trade_compliance.db'

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

@app.route('/api/shipping_documents', methods=['GET'])
def get_shipping_documents():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS documents (id INTEGER PRIMARY KEY, name TEXT)')
    cursor.execute('INSERT INTO documents (name) VALUES ("Invoice"), ("Packing List"), ("Bill of Lading")')
    db.commit()
    cursor.execute('SELECT * FROM documents')
    documents = cursor.fetchall()
    return jsonify([{'id': document[0], 'name': document[1]} for document in documents])

if __name__ == '__main__':
    app.run(debug=True)
