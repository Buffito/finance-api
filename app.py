import os
from dotenv import load_dotenv
from flask import Flask
from database.database import db

def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    db. init_app(app)
    
    # import blueprints
    from routes import main as mr
    app.register_blueprint(mr.main)
    return app

def setup_database(flask_app):
    with flask_app.app_context():
        db.create_all()
        
app = create_app();
setup_database(app)

if __name__ == "__main__":
    app.run(host='0.0.0.0')