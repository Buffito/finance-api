from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)