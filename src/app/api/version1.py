#!/usr/bin/env python
""" Routes for the Events application """
import json
import os
import re
from ..lib import logger
from flask import g
from ..lib import constants as INVITE
from flask import request, Blueprint
from flask import Blueprint
from ..workers import functions as app_functions

send = Blueprint('routes', __name__)

# add for testing: methods=['POST']



# --- test endpoint ---#
@send.route('test', methods=['GET'])
def list_events_signups():
    result = app_functions.test()
    return result

# --- error code indexes --- #
@send.errorhandler(404)
def page_not_found(e):
    return '404 error {}'.format(e), 404


@send.errorhandler(500)
def internal_server_error(e):
    return '500 error {} '.format(e), 500


@send.errorhandler(502)
def bad_gateway_error(e):
    return '502 error {}'.format(e), 502


@send.errorhandler(504)
def gateway_timeout_error(e):
    return '504 error {}'.format(e), 504


@send.errorhandler(505)
def bad_gateway_error(e):
    return '505 error {} '.format(e), 505
