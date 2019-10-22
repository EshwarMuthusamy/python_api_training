#!/usr/bin/python3
from requests import get
#import requests
HUSTON = 'http://api.open-notify.org/astros.json'
def main():
    data = get(HUSTON)
    for astro in data.json().get('people'):
        print(astro['name'])
if __name__ == "__main__":
    main()
