#!/usr/bin/env python
import os
import requests, json
import logging


def slack_notify(message):
    logging.info('sending alert to slack')
    slackURL = os.environ.get('BIG_DADDY_WEBHOOK')
    slackpayload = {
        "fallback": message,
        "color": "#36a64f",
        "fields": [
            {
                "title": "Big Daddy",
                "value": message,
                "short": 'false'
            }
        ]
    }
    postdata = {'payload': json.dumps(slackpayload)}
    r = requests.post(slackURL, data=postdata)
    return r.text
