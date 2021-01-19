__version__ = "0.1.0"


import os
from flask import Flask


# Globally accessible libraries
# wtf = WTForm()


def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.DevConfig")

    # Initialize Plugins (if necessary)
    # wtf.init_app(app)

    with app.app_context():
        # Import parts of the application
        from .home import routes
        from .bfi_form import routes

        # Register Blueprints
        app.register_blueprint(home.home_bp)
        app.register_blueprint(bfi_form.form_bp)

        return app
