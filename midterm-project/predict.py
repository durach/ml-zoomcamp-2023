#!/usr/bin/env python

import pickle

from flask import Flask
from flask import request
from flask import jsonify


with open('model_cli.bin', 'rb') as f_in:
    dv, model = pickle.load(f_in)

app = Flask('midterm-project')

@app.route('/predict', methods=['POST'])
def predict():
    patient = request.get_json()

    X = dv.transform([patient])
    y_pred = model.predict_proba(X)[0, 1]
    churn = y_pred >= 0.5

    result = {
        'heartdisease_probability': float(y_pred),
        'heartdisease': bool(churn)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9911)
