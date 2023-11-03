#!/usr/bin/env python

import requests
import argparse

from pprint import pprint

parser = argparse.ArgumentParser()
parser.add_argument('--base-url', default='http://localhost:9911')
args = parser.parse_args()

patient = {
    "age": 40,
    "sex": "M",
    "chestpaintype": "NAP",
    "maxhr": 172, 
    "restingbp": 130,
    "cholesterol": 200,
    "st_slope": "Down",
}

response = requests.post(f"{args.base_url}/predict", json=patient).json()

pprint(response)
