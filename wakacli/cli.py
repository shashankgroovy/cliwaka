#!/usr/bin/env/python
# Encoding: utf-8

import requests
import json

import config
from output import pretty_output

BASE_URL = 'https://wakatime.com/api/v1/'

# get the current user
resource_endpoints = {
    'user': 'users/current',
    'stats': '/stats/last_7_days',
    'summaries' : '/summaries',
    'durations': '/durations',
    'hearbeats': '/heartbeats'
}


def signal_handler(signal, frame):
    """exit gracefully on keybord interrupt"""
    sys.exit(0)

if __name__ == "__main__":


    # handle SIGINT
    import signal
    import sys

    signal.signal(signal.SIGINT, signal_handler)

    # run
    print "Fetching credentials..."
    if config.get_config('api_key'):
        print "API key found."
        API_KEY = config.get_config('api_key')
    else:
        API_KEY = config.setup_config()

    params = {"api_key": API_KEY}
    endpoint = resource_endpoints['user']

    r = requests.get(BASE_URL + endpoint, params=params)
    print pretty_output(json.dumps(r.json()))
