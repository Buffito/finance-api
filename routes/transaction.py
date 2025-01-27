from flask import Blueprint, request, jsonify
from marshmallow import Schema, fields, ValidationError
from database.database import db
from datetime import datetime
from database.models import Transaction, TransactionType

transaction = Blueprint('transaction', __name__)

class TransactionTypeSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str()

class TransactionSchema(Schema):
    id = fields.Int(dump_only=True)
    transaction_type = fields.Nested(TransactionTypeSchema)
    amount = fields.Float(required=True)
    at_date = fields.DateTime()

@transaction.route('/transactions', methods=['GET'])
def get_transactions():
    transactions = Transaction.query.all()
    transactions_list = TransactionSchema(many=True).dump(transactions)
    return jsonify(transactions_list), 200

@transaction.route('/transactions', methods=['POST'])
def create_transaction():
    req = request.get_json()
    schema = TransactionSchema()
    try:
        validated_data = schema.load(req)
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

@transaction.route('/transactions/<int:transaction_id>', methods=['PUT'])
def update_transaction(transaction_id):
    return jsonify({"message": "Endpoint not implemented yet"}), 501

@transaction.route('/transactions/<int:transaction_id>', methods=['DELETE'])
def delete_transaction(transaction_id):
    return jsonify({"message": "Endpoint not implemented yet"}), 501