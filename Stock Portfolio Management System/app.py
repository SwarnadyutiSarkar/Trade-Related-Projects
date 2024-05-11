# app.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stocks.db'
db = SQLAlchemy(app)

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(10), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Stock(symbol='{self.symbol}', quantity={self.quantity})"

@app.route('/api/stocks', methods=['GET'])
def get_stocks():
    stocks = Stock.query.all()
    return jsonify([{'id': stock.id, 'symbol': stock.symbol, 'quantity': stock.quantity} for stock in stocks])

@app.route('/api/stocks', methods=['POST'])
def add_stock():
    data = request.json
    new_stock = Stock(symbol=data['symbol'], quantity=data['quantity'])
    db.session.add(new_stock)
    db.session.commit()
    return jsonify({'message': 'Stock added successfully'})

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
