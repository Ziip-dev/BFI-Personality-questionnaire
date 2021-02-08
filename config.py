"""Class-based Flask app configuration."""

from os import environ, path
from dotenv import load_dotenv

# Define the application dierctory
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))


class Config(object):
    """Base config."""

    SECRET_KEY = environ.get("SECRET_KEY")
    FLASK_ENV = environ.get("FLASK_ENV")
    FLASK_APP = "wsgi.py"

    # Static Assets
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"


class ProdConfig(Config):
    DEBUG = False
    TESTING = False
    # SERVER_NAME = If you intend your app to be reachable on a custom domain, we specify the app's domain name here.


class DevConfig(Config):
    DEBUG = True
    TESTING = True
