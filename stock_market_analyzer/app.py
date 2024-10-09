from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

def scrape_stock_data(stock_symbol):
    url = f"https://finance.yahoo.com/quote/{stock_symbol}/history?p={stock_symbol}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Scrape historical data
    table = soup.find('table', {'data-test': 'historical-prices'})
    rows = table.find_all('tr')[1:]  # Skip header

    data = []
    for row in rows:
        cols = row.find_all('td')
        if len(cols) > 1:
            date = cols[0].text
            close = cols[4].text.replace(',', '')  # Close price
            data.append({'Date': date, 'Close': float(close)})

    return pd.DataFrame(data)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        stock_symbol = request.form['stock_symbol']
        df = scrape_stock_data(stock_symbol)

        # Save the plot
        plt.figure(figsize=(10, 5))
        plt.plot(df['Date'], df['Close'], marker='o')
        plt.title(f'{stock_symbol} Historical Prices')
        plt.xlabel('Date')
        plt.ylabel('Close Price ($)')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plot_path = os.path.join('static', f'{stock_symbol}.png')
        plt.savefig(plot_path)
        plt.close()

        return render_template('results.html', stock_symbol=stock_symbol, plot_path=plot_path, data=df.to_html())

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
