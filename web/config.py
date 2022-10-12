import os


class BaseConfig(object):
    DEBUG = os.environ['DEBUG']
    DB_NAME = os.environ['POSTGRES_DB']
    DB_USER = os.environ['POSTGRES_USER']
    DB_PASS = os.environ['POSTGRES_PASSWORD']
    DB_SERVICE = os.environ['POSTGRES_SERVICE']
    DB_PORT = os.environ['DATABASE_PORT']
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASS}@{DB_SERVICE}:{DB_PORT}/{DB_NAME}'
