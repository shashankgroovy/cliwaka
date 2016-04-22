import os
import sys

# set the location of ~/.wakacli.cfg file
DEFAULT_CONFIG_FILE = os.path.join(str(os.environ.get('HOME')) or
                                   str(os.getenv("USERPROFILE")),
                                   ".wakacli.cfg")

def get_config(token):
    """Get auth token values from the config file."""

    if sys.version_info[0] == 3:
        import configparser as cp
    else:
        import ConfigParser as cp

    config = cp.RawConfigParser()
    if not config.read(DEFAULT_CONFIG_FILE):
        return None
    else:
        return config.get('AUTH', token)


def set_config(fields):
    """Set all auth token values in the config file."""

    if sys.version_info[0] == 3:
        import configparser as cp
    else:
        import ConfigParser as cp

    config = cp.RawConfigParser()
    config.add_section('AUTH')
    for token in fields:
        config.set('AUTH', token, fields[token])

    with open(DEFAULT_CONFIG_FILE, 'wb') as configfile:
        config.write(configfile)


def setup_config():
    """Initiate auth setup config."""
    print "Set up credentials."
    api_key  = raw_input("Please Enter your Wakatime API KEY: ").strip()
    set_config({'api_key': api_key})
    return api_key


def update_api_key():
    """update with new api key"""
    api_key  = raw_input("Please Enter your Wakatime API KEY: ")
    set_config({'api_key': api_key})


