from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from . import config
from flask import Flask

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config.Config)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)

# Import application components
    with app.app_context():
        db.create_all()             # create db models within app.context
        from . import home
        from . import auth
        from . import reviews

# Register all Blueprints to be used
    app.register_blueprint(home.home_bp)
    app.register_blueprint(auth.auth_bp)
    app.register_blueprint(reviews.view_bp)

    return app
