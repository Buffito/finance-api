# For testing purposes only

from flask import Blueprint, jsonify
from app.models import TransactionType

transaction_type = Blueprint('transaction_type', __name__)

@transaction_type.route('/transaction-types', methods=['GET'])
def get_transaction_types():
    transaction_types = TransactionType.query.all()
    return jsonify([t.name for t in transaction_types])