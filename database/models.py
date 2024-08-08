from datetime import datetime

from .database import db


class TransactionType(db.Model):  # name of table, flask will translate CamelCase to snake_case "transaction_type"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # primary keys are required by SQLAlchemy
    description = db.Column(db.String(50), nullable=False)


class Transaction(db.Model): # name of table, flask will translate the Name to lowercase "transaction"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # primary keys are required by SQLAlchemy
    type = db.Column(db.Integer, db.ForeignKey('transaction_type.id'), nullable=False)
    amount = db.Column(db.Numeric, nullable=False)
    at_date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
