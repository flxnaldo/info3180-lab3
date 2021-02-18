import os

class Config(object):
    """Base Config Object"""
    DEBUG = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'localhost'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Som3$ec5etK*y'
    MAIL_PORT = os.environ.get('MAIL_PORT') or '25' or '465' or '2525' or '587'
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

class DevelopmentConfig(Config):
    """Development Config that extends the Base Config Object"""
    DEVELOPMENT = True
    DEBUG = True

class ProductionConfig(Config):
    """Production Config that extends the Base Config Object"""
    DEBUG = False
