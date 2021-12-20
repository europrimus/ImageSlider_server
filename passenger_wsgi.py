import os
import sys
import json
from Logger import Logger

sys.path.insert(0, os.path.dirname(__file__))

def application(environ, start_response):
    logger = Logger(__name__)
    logger.info("Start application")
    jsonData={}
    jsonData['scriptFile'] = os.path.basename(__file__)
    jsonData['requestPath'] = environ['REQUEST_URI']
    jsonData['pythonVersion'] = sys.version.split()[0]
    del logger
    start_response('200 OK', [('Content-Type', 'application/json')])
    return [json.dumps(jsonData).encode()]
