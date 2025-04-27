from application.models.user import User
from application.extensions import db

class AuthService:
    @staticmethod
    def register_user(username, password, email=None):
        if User.query.filter_by(username=username).first():
            return False, 'Username already exists'
        
        if email and User.query.filter_by(email=email).first():
            return False, 'Email already in use'
            
        user = User(username=username, email=email)
        user.set_password(password)
        
        db.session.add(user)
        db.session.commit()
        return True, user

    @staticmethod
    def authenticate_user(username, password):
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            return True, user
        return False, 'Invalid credentials'