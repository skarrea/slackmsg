"""
Module for sending slack messages using curl
"""
import json
import os
import argparse
import tempfile

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
	if args.to:
		recipientID = data["channelID"][args.to.lower()]
	else:
		recipientID = data["channelID"][args.toID]
	expression = f'curl -X POST "https://slack.com/api/chat.postMessage" -H  "accept: application/json" -d token="{token}" -d channel="{recipientID}" -d text="{args.msg}" --silent'
	out = os.popen(expression).read()
	status = json.loads(out)
	if args.verbosity == 1:
		if status['ok']:
			print("Message sent sucessfully")
		else:
			print("Ooops. Somehting went wrong. Dumping log\n")
			print(status)
	elif args.verbosity == 2:
		print(status)

	# print(out)
	# os.system('echo')

def main():
	with open(os.path.join(os.path.dirname(__file__), 'data.json'), 'r') as f:
		data = json.load(f)
	args = cmdline_args()
	sendmsg(args, data)
	pass

if __name__ == "__main__":
	main()