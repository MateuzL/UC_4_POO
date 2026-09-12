from flask import Flask
from flask_login import LoginManager
from .data import users
from .routes.auth import auth_bp
from .routes.main import main_bp
from .routes.coordination import coord_bp

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "senac-demo-secret"

    login_manager = LoginManager(app)
    login_manager.login_view = "auth.login"

    @login_manager.user_loader
    def load_user(user_id):
        try:
            return users.get(int(user_id))
        except (TypeError, ValueError):
            return None

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(coord_bp, url_prefix="/coordenacao")
    return app
