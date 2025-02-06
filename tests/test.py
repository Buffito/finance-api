from flask import Blueprint, jsonify
from tests.test_service import TestService
from app.models import TransactionType

test = Blueprint('test', __name__)

@test.route('/transactions', methods=['GET'])
def get_transactions():
    transactions = TestService.get_all_transactions()
    return jsonify(transactions), 200

@test.route('/transaction-types', methods=['GET'])
def get_transaction_types():
    transaction_types = TransactionType.query.all()
    return jsonify([t.name for t in transaction_types])

@test.route('/users', methods=['GET'])
def get_users():
    users = TestService.get_all_users()
    return jsonify(users), 200