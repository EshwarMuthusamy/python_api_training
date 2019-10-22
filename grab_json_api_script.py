#!/usr/bin/python3
import urllib.request as req
import json

HUSTON = 'http://api.open-notify.org/astros.json'

def main():
    ground_ctrl = req.urlopen(HUSTON)
    print("Return code")
    print(ground_ctrl.getcode())
    data_str = ground_ctrl.read()
    data = json.loads(data_str.decode('utf-8'))
    print("Type of var : ",str(type(data)))
    print("Full data \n\n")
    print(data.get('people'))
    print("\n\n Names only")
    for astro in data.get('people'):
        print(astro['name'])

if __name__ == "__main__":
    main()
