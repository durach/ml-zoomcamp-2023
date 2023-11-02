#!/usr/bin/env python

import requests

from pprint import pprint

url = 'http://localhost:9911/predict'

patient = {
    "age": 40,
    "sex": "M",
    "chestpaintype": "NAP",
    "maxhr": 172, 
    "restingbp": 130,
    "cholesterol": 200,
    "st_slope": "Down",
}

response = requests.post(url, json=patient).json()

pprint(response)
