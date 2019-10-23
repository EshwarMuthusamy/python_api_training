#!/usr/bin/python3
""" Written by Eshwar Muthusamy """

import requests

def main():
    """ Code to print out the details in the URL response """

    # define URL
    url = 'https://api.nasa.gov/neo/rest/v1/feed?'
    start_date = 'start_date=2019-10-15'
    end_date = '&end_date=END_DATE'
    api_key = '&api_key='
    with open('/home/student/nasa.creds') as ncreds:
       api_key =  api_key + ncreds.read().rstrip('\n')
    print(api_key)
    # prompt user for start date

    # prompt user for end date

    # make API request
    response = requests.get(url+start_date+api_key)

    # parse out json
    # print(response.json())

    response_json = response.json()

    for response in response_json:
        neo = response_json.get('near_earth_objects')
        # print(type(neo))
        for key in neo:
            dates = neo[key]
            for i in dates:
                if type(i) == dict:
                    print(dates)

if __name__ == "__main__":
    main()
