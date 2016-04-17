import requests
import json

BASE_URL = 'https://wakatime.com/api/v1/'
API_KEY  = raw_input("Enter your api key: ")

# get the current user
resource_endpoints = {
    'current_user': 'users/current',
    'stats': '/stats/last_7_days',
    'summaries' : '/summaries',
    'durations': '/durations',
    'hearbeats': '/heartbeats'
}

# make the requests object

params = {"api_key": API_KEY}
endpoint = resource_endpoints['current_user']
r = requests.get(BASE_URL + endpoint, params=params)

print json.dumps(r.json(), indent=4)
