from app.models import Transaction, TransactionType, User
from app import db
from app.schemas import TransactionSchema
from marshmallow import ValidationError
from datetime import datetime
from flask import jsonify

class TransactionService:
    @staticmethod
    def get_all():
        transactions = Transaction.query.all()
        return TransactionSchema(many=True).dump(transactions)
    
    @staticmethod
    def get_all_by_user_id(user_id):
        transactions = Transaction.query.filter_by(user_id=user_id).all()
        return TransactionSchema(many=True).dump(transactions)

    @staticmethod
    def create_transaction(data):
        schema = TransactionSchema()
        try:
            validated_data = schema.load(data)
        except ValidationError as err:
            return jsonify(err.messages), 400

        transaction_type_id = validated_data['transaction_type']['id']
        transaction_type = TransactionType.query.get(transaction_type_id)
        if not transaction_type:
            return jsonify({"error": "Invalid transaction type ID"}), 400

        user = User.query.get(validated_data['user_id'])
        if not user:
            return jsonify({"error": "Invalid user ID"}), 400

        transaction = Transaction(
            type_id=transaction_type.id, 
            amount=validated_data['amount'],
            at_date=validated_data.get('at_date', datetime.now()),
            user_id=user.id
        )
        
        try:
            db.session.add(transaction)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400
        
        return jsonify(TransactionSchema().dump(transaction)), 201