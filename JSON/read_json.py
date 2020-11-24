import json
from pprint import pprint

filename = input("Enter Filename: ")
with open(filename) as f:
    data = json.load(f)
pprint(data)


