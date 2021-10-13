# https://slack.dev/python-slackclient/basic_usage.html
import json
import os


def slack_logger(event, context):
    # TODO implement
    from slack import WebClient
    from slack.errors import SlackApiError
    slack_token = os.environ["SLACK_API_TOKEN"]
    client = WebClient(token=slack_token)
    message = json.dumps(event)
    channel = os.environ["SLACK_API_CHANNEL"]

    try:
      response = client.chat_postMessage(
        channel=channel,
        text= message
      )
    except SlackApiError as e:
      # You will get a SlackApiError if "ok" is False
      return {
        'statusCode': 503,
        'body': json.dumps(e.response["error"])# str like 'invalid_auth', 'channel_not_found'
      }
    
    return {
        'statusCode': 200,
        'body': json.dumps("message '"+ message + "' sent to channel: '" + channel + "'")
    }