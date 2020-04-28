"""Route contains inital endpoints such as health checks"""
import sys, os
from flask import g
from flask import request

from . import invite

from ..lib import logger
from ..lib import constants as INVITE
from . import helpers as api

DO_NOT_CHECK = []


def _standardize_params(params):
    if not params:
        params = {}

    if 'channel' not in params:
        params['channel'] = ''

    if 'lang_code' not in params:
        params['lang_code'] = ''

    if 'country_code' not in params:
        params['country_code'] = ''

    return params


#
# Api Requirements
#
@invite.before_request
def api_requires():
    logger.debug("Setting up request")
    params = []

    if request.method in ('GET', 'DELETED'):
        # request.args is an ImmutableMultiDict
        params = request.args.copy()

    elif request.method == 'POST':
        if request.is_json:
            params = request.get_json(silent=True)
        else:
            params = request.form.copy()

    g.params = _standardize_params(params)

    if request.url_rule:
        g.params['uri_rule'] = request.url_rule.rule

    g.params['uri_endpoint'] = request.endpoint


#
# Health Check
#
@invite.route('/service/health')
def health_check():
    logger.info('health check')
    return api.success({'msg': 'All systems are up'})




