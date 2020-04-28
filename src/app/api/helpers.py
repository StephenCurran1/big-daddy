"""Helper methods common to all api entry points"""
import uuid
import functools
import datetime
import os
from flask import g
from flask import Response
from flask import json
from ..lib import logger


def error_message(code, msg, field=''):
    return {
        'code': code,
        'message': msg,
        'field': field
    }


def success(data, status_code=200, **kwargs):  # pragma: no cover
    _resp = {
        'status': kwargs.get('status', 'success'),
        'data': data,
        'message': kwargs.get('message', '')
    }

    return Response(json.dumps(_resp), status_code)


