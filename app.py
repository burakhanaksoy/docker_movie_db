from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Globally accessible libraries
db = SQLAlchemy()

def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    # Initialize Plugins
    db.init_app(app)
    # r.init_app(app)

    with app.app_context():
        # Include our Routes
        # from . import routes

        # Register Blueprints
        # app.register_blueprint(auth.auth_bp)
        # app.register_blueprint(admin.admin_bp)

        # Migration
        migrate = Migrate(app, db)

        # No need for this
        # Should be taken care of by migrate
        # Create tables for our models
        # db.create_all()

        return app