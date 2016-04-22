import signal
import sys
import argparse
import cli

# handle SIGINT
def signal_handler(signal, frame):
    """exit gracefully on keybord interrupt"""
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

parser = argparse.ArgumentParser(prog="Cliwaka", description="A command line tool for wakatime.com.",
                                    epilog="For more information see http://github.com/shashankgroovy/cliwaka")

parser.add_argument("-b", "--heartbeat", help="show user's latest heartbeat",
                    action="store_true")
parser.add_argument("-d", "--duration", help="show user's logged time for a given day",
                    action="store_true")
parser.add_argument("-t", "--stats", help="show user's current stats.",
                    action="store_true")
parser.add_argument("-s", "--summary", help="show user's logged time.",
                    action="store_true")

parser.add_argument("--leaderboard", help="display the public leaderboard",
                    action="store_true")

parser.add_argument("-v", "--verbose", help="toggle verbose on (default is off)",
                    action="store_true")
parser.add_argument('-V', '--version', action='version', version='%(prog)s 0.1')
args = parser.parse_args()

if args.verbose:
    print "verbose is on"
elif args.heartbeat:
    cli.get_heartbeats()
elif args.duration:
    cli.get_durations()
elif args.stats:
    cli.get_stats()
elif args.summary:
    cli.get_summaries()
elif args.leaderboard:
    cli.view_leaderboard()
else:
    cli.view_user()
