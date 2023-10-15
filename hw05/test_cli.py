#!/usr/bin/env python

import pickle

with open('model1.bin', 'rb') as f_in:
    model = pickle.load(f_in)

with open('dv.bin', 'rb') as f_in:
    dv = pickle.load(f_in)

client = {
    "job": "retired", 
    "duration": 445, 
    "poutcome": "success"
}

X = dv.transform([client])
y_pred = model.predict_proba(X)[0, 1]

print(round(y_pred, 3))
