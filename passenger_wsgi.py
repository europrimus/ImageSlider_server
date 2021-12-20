import os
import sys
import json

sys.path.insert(0, os.path.dirname(__file__))


def application(environ, start_response):
    logging.debug("environ : {}".format(environ))
    jsonData={}
    jsonData['scriptFile'] = os.path.basename(__file__)
    jsonData['requestPath'] = environ['REQUEST_URI']
    jsonData['pythonVersion'] = sys.version.split()[0]
    start_response('200 OK', [('Content-Type', 'application/json')])
    return [json.dumps(jsonData).encode()]
