from flask import Flask, jsonify, redirect
from dotenv import load_dotenv
import os
from flask_sqlalchemy import SQLAlchemy
    
def init_blueprints():
    from blueprints import main as main_blueprint
    app.register_blueprint(main_blueprint.main)
    
def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')

    return app

app = create_app()
db = SQLAlchemy(app)
    
init_blueprints()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105, debug=True)