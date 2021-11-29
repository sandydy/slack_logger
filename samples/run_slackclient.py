# https://slack.dev/python-slackclient/basic_usage.html
import json
import os
import logging


# TODO implement
from slack import WebClient
from slack.errors import SlackApiError
slack_token = os.environ["SLACK_API_TOKEN"]
client = WebClient(token=slack_token)
message = "test"

channel = os.environ["SLACK_API_CHANNEL"]

try:
    response = client.chat_postMessage(
    channel=channel,
    text= message
    )
except SlackApiError as e:
    # You will get a SlackApiError if "ok" is False
    logging.error(json.dumps(e.response["error"]))# str like 'invalid_auth', 'channel_not_found'


logging.info(json.dumps("message '"+ message + "' sent to channel: '" + channel + "'"))