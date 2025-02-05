from flask import Blueprint, request, jsonify
from app.services import TransactionService
from flask_jwt_extended import jwt_required

transaction = Blueprint('transaction', __name__)

@transaction.route('/transactions/user/<int:user_id>', methods=['GET'])
@jwt_required()
def get_transactions_by_user_id(user_id):
    transactions = TransactionService.get_all_by_user_id(user_id)
    return jsonify(transactions), 200

@transaction.route('/transactions', methods=['POST'])
@jwt_required()
def create_transaction():
    data = request.get_json()
    return TransactionService.create_transaction(data)