import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET KEY') or '11011011'
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
