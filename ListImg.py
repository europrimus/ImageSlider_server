import os
from Logger import Logger

class ListImg(object):
    """ListImg
    list all images from a directory
    """

    def __init__(self, path):
        self.path = os.path.dirname(__file__) + path
        self.logger = Logger(__name__)

    def list(self, prefix = "/"):
        images = []
        for (dirpath, dirnames, filenames) in os.walk(self.path):
            for filename in filenames:
                data = {}
                data['url'] = "{}/{}".format(prefix,filename)
                data['file'] = filename
                images.append(data)
            break
        self.logger.debug("list : {}".format(images))
        return images
