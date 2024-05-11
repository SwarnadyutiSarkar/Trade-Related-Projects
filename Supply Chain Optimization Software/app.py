# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from pulp import LpMaximize, LpProblem, LpVariable

app = Flask(__name__)
CORS(app)

@app.route('/api/optimize', methods=['POST'])
def optimize_supply_chain():
    data = request.json

    # Extracting data from the request
    demand = data['demand']
    supply = data['supply']
    costs = data['costs']

    # Defining decision variables
    variables = LpVariable.dicts("Shipment", ((i, j) for i in supply for j in demand), lowBound=0, cat='Integer')

    # Defining the optimization problem
    prob = LpProblem("SupplyChainOptimization", LpMaximize)

    # Defining objective function
    prob += lpSum([variables[(i, j)] * costs[i][j] for i in supply for j in demand])

    # Adding constraints
    for j in demand:
        prob += lpSum([variables[(i, j)] for i in supply]) == demand[j]

    for i in supply:
        prob += lpSum([variables[(i, j)] for j in demand]) <= supply[i]

    # Solving the optimization problem
    prob.solve()

    # Extracting results
    results = {}
    for v in prob.variables():
        if v.varValue > 0:
            results[v.name] = v.varValue

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
