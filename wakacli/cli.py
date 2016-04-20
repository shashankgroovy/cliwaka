#!/usr/bin/env/python
# Encoding: utf-8

import requests
import json

import config
from output import pretty_output

BASE_URL = 'https://wakatime.com/api/v1/'

resource_endpoints = {
    'stats': '/stats/last_7_days',
    'summaries' : '/summaries',
    'durations': '/durations',
    'heartbeats': '/heartbeats',
    'user_agents': '/user_agents'
    }

def view_user(user="current"):
    """Returns a specific users information and returns the current user by
    default."""
    if user != 'current':
        user = '@' + user
    make_request(user=user)

def view_leaderboard():
    """Returns the public leaderboard.

    A list of users ranked by logged time in descending order."""
    make_request(leader=True)

def get_stats():
    """Returns user's stats and logged time for the given time range.

    Allowed time ranges are:
        last_7_days,            # only a weeks stat is available for free accounts
        last_30_days,
        last_6_months,
        last_year,
        all_time
    """
    pass

def get_summaries(start=None, end=None, project="", branches=""):
    """Returns a user's logged time for the given time range as an array of
    summaries segmented by day."""
    if start == None:
        import datetime
        start = datetime.date.today()

    if end == None:
        import datetime
        end = datetime.date.today()

    endpoint = 'summaries'
    params = {
        'start': start,
        'end': end,
        'project': project,
        'branches': branches
    }
    make_request(endpoint, params)

def get_durations(date=None, project="", branches=""):
    """Returns a user's logged time for the given day as an array of duration
    blocks."""
    if date == None:
        import datetime
        date = datetime.date.today()

    endpoint = 'durations'
    params = {
        'date': date,
        'project': project,
        'branches': branches
    }
    make_request(endpoint, params)

def get_heartbeats(date=None):
    """Returns a user's heartbeats sent from plugins for the given day as an
    array."""
    if date == None:
        import datetime
        date = str(datetime.date.today())

    endpoint = 'heartbeats'
    params = {'date': date}
    make_request(endpoint, params)

def get_user_agents():
    """Returns a list of plugins which have sent data for this user."""
    endpoint = 'user_agents'
    make_request(endpoint)

def make_request(endpoint="", params={}, user="current", leader=False):
    """Generic request wrapper for routing all requests to api"""

    print "Requesting data..."
    API_KEY = config.get_config('api_key') or config.setup_config()

    # make the request parameters and endpoint ready
    params["api_key"] = API_KEY

    if leader == False:
        user_type = 'users/' + user

        if resource_endpoints.has_key(endpoint):
            endpoint = resource_endpoints[endpoint]

        r = requests.get(BASE_URL + user_type + endpoint, params=params)

        if r.status_code == 200:
            print pretty_output(json.dumps(r.json()))
        elif r.status_code == 403:
            print "Whoops! Looks like we can't show that."
        else:
            print "We are having some problem. Make sure you have everything correct."

    else:
        r = requests.get(BASE_URL + 'leaders')
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
    get_user()
