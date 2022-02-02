import os
import mimetypes
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
            filenames.sort()
            for filename in filenames:
                (type, encoding) = mimetypes.guess_type("{}/{}".format(self.path,filename))
                if type != None and type.split("/")[0] == "image":
                    data = {}
                    data['url'] = "{}/{}".format(prefix,filename)
                    data['type'] = type
                    images.append(data)

            break
        self.logger.debug("list : {}".format(images))
        return images
