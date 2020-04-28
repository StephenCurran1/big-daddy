#!/usr/bin/env python
import logging
from app.api import invite


def run_test_app():
    invite.run(host='0.0.0.0', debug=True)

if __name__ == "__main__":
    logging.debug("about to start big daddy flask-app")
    run_test_app()
