from flask import Flask
from dotenv import load_dotenv
import os
from flask_sqlalchemy import SQLAlchemy

def init_app():
    load_dotenv()
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    
    return app


app = init_app()
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105, debug=True)