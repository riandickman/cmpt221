from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)


    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'  
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'ilovefinn'  

    db.init_app(app)

    with app.app_context():
        from . import app  

    return app
