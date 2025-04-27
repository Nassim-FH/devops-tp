from flask import Flask
from config import Config
from application.extensions import db, login_manager,csrf

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    # csrf.init_app(app)
    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    
    # Register blueprints
    from application.controllers.auth import auth_bp
    from application.controllers.main import main_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    
    # User loader
    from application.models.user import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    return app