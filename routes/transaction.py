from flask import Blueprint, request, jsonify

transaction = Blueprint('transaction', __name__)

@transaction.route('/transactions', methods=['GET'])
def get_transactions():
   return jsonify({"message": "Not implemented yet"}), 501

@transaction.route('/transactions', methods=['POST'])
def create_transaction():
    return jsonify({"message": "Not implemented yet"}), 501

@transaction.route('/transactions/<int:transaction_id>', methods=['PUT'])
def update_transaction(transaction_id):
    return jsonify({"message": "Not implemented yet"}), 501

@transaction.route('/transactions/<int:transaction_id>', methods=['DELETE'])
def delete_transaction(transaction_id):
    return jsonify({"message": "Not implemented yet"}), 501