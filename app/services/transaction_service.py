from app.models import Transaction
from app import db
from app.schemas import TransactionSchema
from marshmallow import ValidationError
from datetime import datetime
from flask import jsonify

class TransactionService:
    @staticmethod
    def get_all():
        transactions = Transaction.query.all()
        transactions_list = TransactionSchema(many=True).dump(transactions)
        return transactions_list

    @staticmethod
    def create_transaction(transaction):
        schema = TransactionSchema()
        try:
            validated_data = schema.load(transaction)
        except ValidationError as err:
            return jsonify(err.messages), 400

        transaction = Transaction(
            type_id=validated_data['transaction_type']['id'], 
            amount=validated_data['amount'],
            at_date=validated_data.get('at_date', datetime.now())
        )
        
        try:
            db.session.add(transaction)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400
        
        return jsonify(TransactionSchema().dump(transaction)), 201