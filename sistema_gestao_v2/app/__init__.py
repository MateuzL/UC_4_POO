from flask import Flask
from flask_login import LoginManager
from config import Config
from .data import init_demo_data

login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.login_message = "Faça login para continuar."

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    login_manager.init_app(app)

    from .routes.auth import auth_bp
    from .routes.main import main_bp
    from .routes.coordination import coord_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(coord_bp)

    with app.app_context():
        init_demo_data()

    return app
