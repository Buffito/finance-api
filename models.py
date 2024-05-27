from app import db

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Double, nullable=False)
    date = db.Column(db.DateTime, nullable=False)