# Slack wrapper
This is a simple python command line interface that wraps the python slack SDK to be able to send slack messages from the command line.

## Requirements
The guide is written for linux based systems. It can be adapted to other operating systems.

## Installation
### Follow the slack tutorial
Follow the slack guide on [Posting messages using curl](https://api.slack.com/tutorials/tracks/posting-messages-with-curl) to set up a bot in your workspace with the right permissions. Remember to give the bot permission to send private messages by setting the **Messages Tab** in **App Home** on. 

After you're finished setting up the bot you should be able to post a chat message using
```curl -d "text=Hi I am a bot that can post messages to any public channel." -d "channel=C123456" -H "Authorization: Bearer xoxb-not-a-real-token-this-will-not-work" -X POST https://slack.com/api/chat.postMessage```

where you need to change `token` to the bots `token` and `channel` to the channel ID to which you want to send the message. If the message is sent and received successfully we're ready for the next step.

### Set up the environment variables
We need a place to store channel IDs and the bots access token. For this we create a `.json` file and point to it with an environment variable called `SLACKDATA`. The `.json` file should look like this
```
{
	"channelID" : {
		"user1" : "channelIDForUser1"
		"user2" : "channelIDForUser2"
		"channel1" : "channelIDForChannel1"
	},
	"token" : "xoxb-not-a-real-token-this-will-not-work"
}
```
where `token` is replaced with the `token` of the bot and `channelID` contains pairs of `users` or `channels` as keys and `userIDs` or `channelIDs` as values. The `.json` file can have an arbitrary name, but we'll call it `.slackdata` in this example. Start by adding a couple of users/channels. We can add more later.

Next we add set the environment variable. For a user this can be done in the `~/.bashrc` by adding the line 
```export SLACKDATA="/path/to/.slackdata"``` 
and sourcing the `~/.bashrc`.
The environment variable can also be set system wide in `/etc/environment`.

### Install
Install the package with
`python3 setup.py install`

## Examples
The send the message `Hello, world!` to `user1` run 
```slackmsg -t user1 -m "Hello, world!```
