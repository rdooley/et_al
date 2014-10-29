#!/usr/bin/env python
"""
Basic web server thing
"""
from bottle import request, response, debug, run, error, route, static_file
import bottle
import logging
import json
import os


FRONT_END_DIR = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')), 'front_end')


@error(400)
def error400(error):
    logging.info('AN ERROR HAS OCCURED')
    return bottle.HTTPResponse(json.dumps({
        'error': error.body
    }), error.status)


@error(404)
def error404(error):
    return error400(error)


# To aid local development:
@route('/')
@route('/<filepath:path>')
def server_static(filepath="index.html"):
    return static_file(filepath, root=FRONT_END_DIR)


def main():
    # It will just run on 8080 by default
    debug(True)
    run(reloader=True)


if __name__ == "__main__":
    sys.exit(main())
