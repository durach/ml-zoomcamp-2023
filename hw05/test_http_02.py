#!/usr/bin/env python

import requests


url = 'http://localhost:1234/predict'

client = {
    "job": "retired", 
    "duration": 445, 
    "poutcome": "success"
}

response = requests.post(url, json=client).json()
print(round(response["score"], 3))
