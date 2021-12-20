import os
from datetime import datetime

class Logger(object):
    def __init__(self,name = __name__):
        filePath = "/home/europrimus/logs/img.europrimus.ninja-python.log"
        self.logFile = open(filePath, "a")
        self.name = name

    def __del__(self):
        self.close()

    def trace(self,message):
        self.logFile.write(self.formatMessage("TRACE",message))
    def debug(self,message):
        self.logFile.write(self.formatMessage("DEBUG",message))
    def info(self,message):
        self.logFile.write(self.formatMessage("INFO",message))
    def warn(self,message):
        self.logFile.write(self.formatMessage("WARN",message))
    def error(self,message):
        self.logFile.write(self.formatMessage("ERROR",message))
    def fatal(self,message):
        self.logFile.write(self.formatMessage("FATAL",message))

    def formatMessage(self,level,message):
        now = datetime.now()
        date = now.strftime("%Y-%m-%d %H:%M:%S")
        return "[{0}][{3}][{1}]{2}\n".format(date,level,message,self.name)

    def close(self):
        self.logFile.close()
        self.logFile = None
