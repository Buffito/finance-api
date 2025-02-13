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

@transaction.route('/transactions/user/<int:user_id>/between', methods=['GET'])
@jwt_required()
def get_transactions_by_user_id_between_dates(user_id):
    data = request.get_json()
    start_date = data.get('start_date')
    end_date = data.get('end_date')
    if not start_date:
        start_transaction = TransactionService.get_first_transaction_by_user_id(user_id)
        start_date = start_transaction.date
    if not end_date:
        end_transaction = TransactionService.get_last_transaction_by_user_id(user_id)
        end_date = end_transaction.date
    transactions = TransactionService.get_all_by_user_id_between_dates(user_id, start_date, end_date)
    return jsonify(transactions), 200