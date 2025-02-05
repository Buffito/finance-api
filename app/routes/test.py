from flask import Blueprint, jsonify
from app.services import TransactionService, UserService
from app.models import TransactionType

test = Blueprint('test', __name__)

@test.route('/transactions', methods=['GET'])
def get_transactions():
    transactions = TransactionService.get_all()
    return jsonify(transactions), 200

@test.route('/transaction-types', methods=['GET'])
def get_transaction_types():
    transaction_types = TransactionType.query.all()
    return jsonify([t.name for t in transaction_types])

@test.route('/users', methods=['GET'])
def get_users():
    users = UserService.get_all()
    return jsonify(users), 200