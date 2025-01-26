import os
from dotenv import load_dotenv
from flask import Flask
from database.database import db

def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    db.init_app(app)
    
    # Register blueprints
    register_blueprints(app)
    
    return app

def register_blueprints(app):
    from routes import main as main_route
    from routes import transaction as transaction_route
    from routes import transaction_type as transaction_type_route
    
    app.register_blueprint(main_route.main)
    app.register_blueprint(transaction_route.transaction)
    app.register_blueprint(transaction_type_route.transaction_type)
    
def setup_database(flask_app):
    with flask_app.app_context():
        try:
            db.create_all()
        except Exception as e:
            print(f"Database setup failed: {e}")
        
app = create_app()
setup_database(app)

if __name__ == "__main__":
    app.run(host='0.0.0.0')