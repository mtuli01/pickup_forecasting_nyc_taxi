import os
import secrets

class Config(object):
    NAME = 'NYC Yellow Taxi Density Prediction'

    TESTING = False
    DEBUG = True

    VERSION = '1.0.0'

    STATIC_FOLDER = 'static'
    MAX_CONTENT_LENGTH = 25 * 1024 * 1024


class Development(Config):
    FLASK_CONFIG = 'development'

    SECRET_KEY = 'development'


class Production(Config):
    FLASK_CONFIG = 'production'

    DEBUG = False

    SECRET_KEY = os.getenv('SECRET_KEY', secrets.token_urlsafe(32))


class Testing(Config):
    FLASK_CONFIG = 'testing'

    TESTING = True

    SECRET_KEY = 'testing'