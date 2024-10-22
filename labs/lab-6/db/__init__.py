from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize the database
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configure the application
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'  # Replace with your database URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'ilovefinn'  # Replace with a random secret key

    # Initialize the database with the app
    db.init_app(app)

    # Import your routes here to avoid circular imports
    with app.app_context():
        from . import app  # Ensure to import your app routes

    return app
