"""
Module for sending slack messages using curl
"""
import json
import os
import argparse
import logging
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

def cmdline_args():
		# Make parser object
	p = argparse.ArgumentParser(description=__doc__,
		formatter_class=argparse.RawDescriptionHelpFormatter)
	
	group1 = p.add_mutually_exclusive_group(required=True)
	group1.add_argument("-t", "--to", type=str,
				   help="Recipient name")
	group1.add_argument("--toID", type=str,
				   help="Recipient channelID")
	p.add_argument("-m", "--msg", type=str,
				   help="message")
	p.add_argument("-v", "--verbosity", type=int, choices=[0,1,2], default=1,
				   help="increase output verbosity (default: %(default)s)")

	return(p.parse_args())

def sendmsg(args, data):
	token = data["token"]

	if args.verbosity == 1:
		logging.basicConfig(level=logging.WARNING)
	elif args.verbosity == 2:
		logging.basicConfig(level=logging.DEBUG)
	elif args.verbosity == 0:
		logging.basicConfig(level=logging.ERROR)

	if args.to:
		recipientID = data["channelID"][args.to.lower()]
	else:
		recipientID = data["channelID"][args.toID]

	client = WebClient(token=token)

	try:
		response = client.chat_postMessage(
			channel=recipientID,
			text=args.msg
		)
	except SlackApiError as e:
		# You will get a SlackApiError if "ok" is False
		assert e.response["error"]    # str like 'invalid_auth', 'channel_not_found'
	# print(out)
	# os.system('echo')

def main():
	with open(os.environ['SLACKDATA'], 'r') as f:
		data = json.load(f)
	args = cmdline_args()
	sendmsg(args, data)
	pass

if __name__ == "__main__":
	main()