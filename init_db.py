from application import create_app
from application.extensions import db

app = create_app()

with app.app_context():
    db.drop_all()  # Clean slate
    db.create_all()  # Create all tables
    print("Database tables created successfully!")