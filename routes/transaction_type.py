from flask import Blueprint, request, jsonify

transaction_type = Blueprint('transaction_type', __name__)

@transaction_type.route('/transaction_types', methods=['GET'])
def get_transaction_types():
   return jsonify({"message": "Not implemented yet"}), 501

@transaction_type.route('/transaction_types', methods=['POST'])
def create_transaction_type():
    return jsonify({"message": "Not implemented yet"}), 501

@transaction_type.route('/transaction_types/<int:transaction_type_id>', methods=['PUT'])
def update_transaction_type(transaction_type_id):
    return jsonify({"message": "Not implemented yet"}), 501

@transaction_type.route('/transaction_types/<int:transaction_type_id>', methods=['DELETE'])
def delete_transaction_type(transaction_type_id):
    return jsonify({"message": "Not implemented yet"}), 501