from . import config
from flask import Flask, Blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object(config.Config)


        # Import application components
    with app.app_context():
        from .home import home
        from .authenticate import auth
        from .reviews import reviews

        # Register all Blueprints to be used
    app.register_blueprint(home.home_bp)
    app.register_blueprint(auth.auth_bp)
    app.register_blueprint(reviews.view_bp)

    return app