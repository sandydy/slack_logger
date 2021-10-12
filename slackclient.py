# https://slack.dev/python-slackclient/basic_usage.html
import logging
logging.basicConfig(level=logging.DEBUG)

import os
from slack import WebClient
from slack.errors import SlackApiError

slack_token = os.environ["SLACK_API_TOKEN"]
client = WebClient(token=slack_token)

try:
  response = client.chat_postMessage(
    channel=os.environ["SLACK_CHANNEL"],
    text=os.environ["SLACK_MESSAGE"]
  )
except SlackApiError as e:
  # You will get a SlackApiError if "ok" is False
  assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
