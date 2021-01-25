__version__ = "0.1.0"

"""Initialize app."""
import os
from flask import Flask
from flask_assets import Environment
from .assets import compile_assets

assets = Environment()

# Globally accessible libraries
# wtf = WTForm()


def create_app():
    """Construct core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.DevConfig")

    # Initialize Plugins (if necessary)
    # wtf.init_app(app)

    with app.app_context():
        # Import parts of the application
        from .home import home
        from .bfi_form import form

        # Register Blueprints
        app.register_blueprint(home.home_bp)
        app.register_blueprint(bfi_form.form_bp)

        return app
