#!/usr/bin/env python

import requests


url = 'http://localhost:1234/predict'

client = {
    "job": "unknown", 
    "duration": 270, 
    "poutcome": "failure"
}

response = requests.post(url, json=client).json()
print(round(response["score"], 3))
