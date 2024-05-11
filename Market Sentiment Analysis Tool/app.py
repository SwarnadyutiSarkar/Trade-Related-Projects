# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from textblob import TextBlob

app = Flask(__name__)
CORS(app)

@app.route('/api/sentiment', methods=['POST'])
def analyze_sentiment():
    data = request.json
    text = data['text']
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    return jsonify({'sentiment': sentiment})

if __name__ == '__main__':
    app.run(debug=True)
