from flask import Flask
from app.config import load_configurations, configure_logging
from .views import webhook_blueprint

def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)

    @app.route('/healthz')
    def home():
        return 'Hello, World!'

    # Load configurations and logging settings
    load_configurations(app)
    configure_logging()

    # Import and register blueprints, if any
    app.register_blueprint(webhook_blueprint)

    return app
