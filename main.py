import base64
import json
import logging

from slack_sdk import WebClient

from config import SLACK_BOT_TOKEN, SLACK_DEFAULT_CHANNEL

logging.basicConfig(level=logging.INFO)


def send_slack_message(channel_name: str, message: str):
    client = WebClient(token=SLACK_BOT_TOKEN)
    client.chat_postMessage(channel=channel_name, text=message)


def main(event, context):

    slack_channel = SLACK_DEFAULT_CHANNEL

    payload_base64 = event["data"]
    payload = base64.b64decode(payload_base64).decode("utf-8")
    payload_json = json.loads(payload)

    function_name = payload_json["function_name"]
    error_message = payload_json["error_message"]

    if "slack_channel" in payload_json:
        slack_channel = payload_json["slack_channel"]

    message = f"Error in cloud function: [{function_name}]. Error message: [{error_message}]"

    send_slack_message(slack_channel, message)




