# main.py
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/trade_data', methods=['GET'])
def get_trade_data():
    # Implement logic to fetch trade data from the database or external API
    trade_data = [
        {"country": "USA", "export_value": 1000000, "import_value": 800000},
        {"country": "China", "export_value": 900000, "import_value": 950000},
        # Add more trade data here
    ]
    return jsonify(trade_data)

if __name__ == '__main__':
    app.run(debug=True)
