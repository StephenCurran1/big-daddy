
"""init file for event application"""
import os
import datadog
from . import version1
from flask import Flask  # pragma: no cover
from ..lib import logger

from . import version1

datadog_options = {
    'statsd_host': os.environ.get('STATSD_HOST', 'statsd.monitoring'),
    'statsd_port': os.environ.get('STATSD_PORT', '8125')
}

datadog.initialize(**datadog_options)
logger.debug("statsd initialized")

invite = Flask(__name__)
invite.register_blueprint(version1.send, url_prefix='/v1')
logger.info("Invite started")

from . import routes


