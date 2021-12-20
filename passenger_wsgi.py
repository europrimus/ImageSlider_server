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
    jsonData = listImg.list(environ['SCRIPT_URI'])
    del logger
    start_response('200 OK', [('Content-Type', 'application/json')])
    return [json.dumps(jsonData).encode()]
