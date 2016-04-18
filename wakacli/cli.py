#!/usr/bin/env/python
# Encoding: utf-8

import requests
import json

import config
from output import pretty_output

BASE_URL = 'https://wakatime.com/api/v1/'

# get the current user
resource_endpoints = {
    'current_user': 'users/current',
    'stats': '/stats/last_7_days',
    'summaries' : '/summaries',
    'durations': '/durations',
    'hearbeats': '/heartbeats'
}

def get_user(user="current"):
    """Returns a specific users information and returns the current user by
    default."""
    pass

def get_stats():
    """Returns current users information"""
    pass

def get_summaries():
    """Returns current users information"""
    pass

def get_durations(date=None, project="", branches=""):
    """Returns a user's logged time for the given day as an array of duration
    blocks."""
    if date == None:
        import datetime
        date = str(datetime.date.today())

    endpoint = resource_endpoints['durations']
    params = {'date': date}
    make_request(endpoint, params)

def request_heartbeats():
    """Returns current users information"""
    pass

def make_request(params={}, endpoint="current_user"):
    """Generic request wrapper for routing all requests to api"""

    print "Requesting data"
    if config.get_config('api_key'):
        print "API key found."
        API_KEY = config.get_config('api_key')
    else:
        print "API key not found."
        API_KEY = config.setup_config()

    # make the request parameters and endpoint ready
    params["api_key"] = API_KEY
    endpoint = resource_endpoints[endpoint]

    r = requests.get(BASE_URL + endpoint, params=params)
    print pretty_output(json.dumps(r.json()))


# handle SIGINT
def signal_handler(signal, frame):
    """exit gracefully on keybord interrupt"""
    sys.exit(0)


if __name__ == "__main__":

    # handle SIGINT
    import signal
    import sys

    signal.signal(signal.SIGINT, signal_handler)

    # run
    make_request()
