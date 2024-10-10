from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_loan_cost(principal, rate, years):
    monthly_rate = rate / 100 / 12
    months = years * 12
    if monthly_rate == 0:
        return principal / months
    monthly_payment = principal * (monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
    total_cost = monthly_payment * months
    return total_cost

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        loans = []
        for i in range(int(request.form['number_of_loans'])):
            principal = float(request.form[f'principal_{i}'])
            rate = float(request.form[f'rate_{i}'])
            years = int(request.form[f'years_{i}'])
            total_cost = calculate_loan_cost(principal, rate, years)
            loans.append({'principal': principal, 'rate': rate, 'years': years, 'total_cost': total_cost})
        return render_template('index.html', loans=loans)

    return render_template('index.html', loans=None)

if __name__ == '__main__':
    app.run(debug=True)
