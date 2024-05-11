# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from sklearn.linear_model import LinearRegression
import numpy as np

app = Flask(__name__)
CORS(app)

@app.route('/api/forecast', methods=['POST'])
def forecast():
    data = request.json

    # Assuming the data consists of two arrays: 'years' and 'values'
    years = np.array(data['years']).reshape(-1, 1)
    values = np.array(data['values'])

    model = LinearRegression()
    model.fit(years, values)

    # Forecasting for the next 5 years
    future_years = np.array(range(max(data['years']) + 1, max(data['years']) + 6)).reshape(-1, 1)
    forecast_values = model.predict(future_years)

    return jsonify({'years': future_years.flatten().tolist(), 'forecast': forecast_values.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
