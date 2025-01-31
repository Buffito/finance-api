from flask import Blueprint, request, jsonify
from app.services import TransactionService

transaction = Blueprint('transaction', __name__)

@transaction.route('/transactions', methods=['GET'])
def get_transactions():
    transactions = TransactionService.get_all()
    return jsonify(transactions), 200

@transaction.route('/transactions/user/<int:user_id>', methods=['GET'])
def get_transactions_by_user_id(user_id):
    transactions = TransactionService.get_all_by_user_id(user_id)
    return jsonify(transactions), 200

@transaction.route('/transactions', methods=['POST'])
def create_transaction():
    data = request.get_json()
    return TransactionService.create_transaction(data)