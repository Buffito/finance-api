from .database import db
from dataclasses import dataclass
from datetime import datetime

@dataclass
class TransactionType(db.Model): #for example income, expense, etc
    __tablename__ = 'transaction_types'
    
    id: int
    name: str
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    
    transactions = db.relationship('Transaction', backref='Transaction_type', lazy=True)

    def __init__(self, name):
        self.name = name
        
@dataclass
class Transaction(db.Model):
    __tablename__ = 'transactions'
    
    id: int
    type_id: int
    amount: float
    at_date: datetime
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type_id = db.Column(db.Integer, db.ForeignKey('transaction_types.id'), nullable=False)
    amount = db.Column(db.Numeric, nullable=False)
    at_date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    
    type = db.relationship('TransactionType', backref='Transaction', lazy=True)
    
    def __init__(self, type_id, amount, at_date):
        self.type_id = type_id
        self.amount = amount
        self.at_date = at_date