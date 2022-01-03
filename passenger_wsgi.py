import os
import sys
import json
from ListImg import ListImg
from Logger import Logger

sys.path.insert(0, os.path.dirname(__file__))

def application(environ, start_response):
    logger = Logger(__name__)
    logger.info("Start application")
    listImg = ListImg(environ['REQUEST_URI'])
    if 'SCRIPT_URI' in environ :
        baseUrl = environ['SCRIPT_URI']
    else :
        baseUrl = "{}://{}{}".format(
            "https" if environ['SERVER_PORT'] == '443' else "http",
            environ['SERVER_NAME'],
            environ['REQUEST_URI']
            )
    jsonData = listImg.list(baseUrl)
    del logger
    start_response('200 OK', [
        ('Content-Type', 'application/json'),
        ('Access-Control-Allow-Origin', '*')
        ])
    return [json.dumps(jsonData).encode()]
