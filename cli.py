#!/usr/bin/env/python
# Encoding: utf-8

import requests
import json

from pygments import highlight, lexers, formatters

BASE_URL = 'https://wakatime.com/api/v1/'
API_KEY  = raw_input("Enter your api key: ")

# get the current user
resource_endpoints = {
    'user': 'users/current',
    'stats': '/stats/last_7_days',
    'summaries' : '/summaries',
    'durations': '/durations',
    'hearbeats': '/heartbeats'
}


# output
DEFAULT_INDENT = 4

def format_output(data, sort=False):
    try:
        obj = json.loads(data)
    except JSONDecodeError:
        pass # Invalid JSON, ignore.
    else:
        # Indent, sort keys by name and avoid unicode escapes to improve
        # readability.
        data = json.dumps(
            obj=obj,
            sort_keys=sort,
            #ensure_ascii=False,
            indent=DEFAULT_INDENT
        )
        pretty_json = highlight(
                        unicode(data, 'UTF-8'),
                        lexers.JsonLexer(),
                        formatters.TerminalFormatter()
                    )
    return pretty_json

if __name__ == "__main__":

    # demo run
    params = {"api_key": API_KEY}
    endpoint = resource_endpoints['user']

    r = requests.get(BASE_URL + endpoint, params=params)
    print format_output(json.dumps(r.json()))
