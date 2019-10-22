#!/usr/bin/python3
"""
Harvest APOD from NASA and print neatly
Written by Eshwar Muthusamy
"""

import requests

## define URL as global
NASA = 'https://api.nasa.gov/planetary/apod?api_key='

def main():
    """ Code to talk to NASA APOD """
    ## read in our NASA api key
    with open('/home/student/nasa.creds', 'r') as ncreds:
        nasa_api_key = ncreds.read()
    print(nasa_api_key)

    ## append to our URL
    final_url = NASA + nasa_api_key.rstrip('\n')
    print(final_url)
    ## make an API request
    response = requests.get(final_url)
    response_json = response.json()
    ## parse out json
    print(response_json)

    ## print out date
    print(response_json.get('date'))
    ## print out explanation
    print(response_json.get('explanation'))
    ## print out URL
    print(response_json.get('hdurl'))

if __name__ == "__main__":
    main()
