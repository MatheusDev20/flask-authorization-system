import os
from dotenv import load_dotenv
load_dotenv()

DEFAULT_DATABASE_URI = 'postgresql+psycopg2://postgres:docker123@localhost:5434/library_manager'


class BaseConfiguration:
    TESTING = False
    SOME_RANDOM_TOKEN = '123'
    SECRET_KEY = 'a88e719e07be687a817aa6a556437a47'

class DevelopmentConfig(BaseConfiguration):
    DEBUG = True
    ENV = 'dev'
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', DEFAULT_DATABASE_URI)
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    TEMPLATES_AUTO_RELOAD = True
    UPLOAD_FOLDER = 'uploads'
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', '')
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', '')

class ProductionConfig(BaseConfiguration):
    DEBUG = False
    TESTING = True
    ENV = 'production'
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', DEFAULT_DATABASE_URI)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config_obj = {
    'dev': 'app.config.DevelopmentConfig',
    'prod': 'app.config.ProductionConfig'
}

def configure_app(app):
    """ Configure the Flask WSGI Instance according the enviroment Variable FLASK_CONF """
    load_dotenv()
    enviroment = os.getenv('FLASK_CONFIG', 'dev')
    app.config.from_object(config_obj[enviroment])
