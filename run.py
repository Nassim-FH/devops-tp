# In run.py or a separate initialization script
from application import create_app
from application.extensions import db

app = create_app()

@app.before_request
def initialize_database():
    with app.app_context():
        db.create_all()  # Creates all database tables

if __name__ == '__main__':
    app.run(debug=True)