# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
# THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
# CSRF_ENABLED     = True

# Use a secure, unique and absolutely secret key for
# signing the data.
# CSRF_SESSION_KEY = "secret"


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
    # SESSION_COOKIE_NAME = environ.get("SESSION_COOKIE_NAME")
    FLASK_APP = "wsgi.py"

    # Static Assets
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"

    # Flask-assets variables
    LESS_BIN = "/usr/bin/lessc"
    ASSETS_DEBUG = False
    ASSETS_AUTO_BUILD = True


class ProdConfig(Config):
    DEBUG = False
    TESTING = False
    # SERVER_NAME = If you intend your app to be reachable on a custom domain, we specify the app's domain name here.


class DevConfig(Config):
    DEBUG = True
    TESTING = True
