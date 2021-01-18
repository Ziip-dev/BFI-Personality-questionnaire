__version__ = "0.1.0"


import os
from flask import Flask


# Globally accessible libraries
# wtf = WTForm()


# def create_app(test_config=None):

#     # create and configure the WSGI application object
#     app = Flask(__name__, instance_relative_config=True)
#     app.config.from_mapping(
#         SECRET_KEY="dev",
#         # DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
#     )

#     if test_config is None:
#         # load the instance config, if it exists, when not testing
#         app.config.from_pyfile("config.py", silent=True)
#     else:
#         # load the test config if passed in
#         app.config.from_mapping(test_config)

#     # ensure the instance folder exists
#     try:
#         os.makedirs(app.instance_path)
#     except OSError:
#         pass

#     from . import views

#     return app


def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")

    # Initialize Plugins (if necessary)
    # wtf.init_app(app)

    with app.app_context():
        # Include all Routes
        from . import routes

        # Register Blueprints
        # app.register_blueprint(auth.auth_bp)
        # app.register_blueprint(admin.admin_bp)

        return app
