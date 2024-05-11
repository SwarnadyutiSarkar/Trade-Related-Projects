# app.py
from flask import Flask, jsonify
from flask_cors import CORS
import plotly.graph_objs as go
import pandas as pd

app = Flask(__name__)
CORS(app)

@app.route('/api/data')
def get_financial_data():
    # Sample financial data (can be replaced with real data)
    data = {
        'Date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05'],
        'Open': [100, 102, 103, 101, 105],
        'Close': [102, 104, 105, 100, 106],
        'Volume': [1000, 1200, 1300, 1100, 1500]
    }

    df = pd.DataFrame(data)
    
    # Create traces for visualization
    trace_open = go.Scatter(x=df['Date'], y=df['Open'], mode='lines', name='Open')
    trace_close = go.Scatter(x=df['Date'], y=df['Close'], mode='lines', name='Close')
    trace_volume = go.Bar(x=df['Date'], y=df['Volume'], name='Volume')

    # Create figure
    fig = go.Figure([trace_open, trace_close, trace_volume])
    fig.update_layout(title='Financial Data Visualization Dashboard', xaxis_title='Date', yaxis_title='Value')

    return jsonify(fig.to_json())

if __name__ == '__main__':
    app.run(debug=True)
