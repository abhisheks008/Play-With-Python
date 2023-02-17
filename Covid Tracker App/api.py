import os
import requests
from dotenv import load_dotenv

load_dotenv()

def getStateInfo(stateName):
    url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"

    querystring = {"country":"India"}

    headers = {
        "X-RapidAPI-Key": os.getenv('API_KEY'),
        "X-RapidAPI-Host": os.getenv('API_HOST')
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    response = response.json()
    StateData = (response['data']['covid19Stats'])

    for my_dict in StateData:
        if my_dict['province'] == stateName:
            data = [my_dict['province'], my_dict['confirmed'], my_dict['deaths'], my_dict['lastUpdate']]
            return data
    else:
        return 0