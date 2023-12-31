__version__ = "0.1.0"

"""Initialize app."""
from flask import Flask


def create_app():
    """Construct core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.ProdConfig")

    with app.app_context():
        # Import parts of the application
        from .bfi_questionnaire import questionnaire_routes

        # Register Blueprints
        app.register_blueprint(questionnaire_routes.questionnaire_bp)

        return app
