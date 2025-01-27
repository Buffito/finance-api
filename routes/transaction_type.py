from flask import Blueprint, request, jsonify
from marshmallow import Schema, fields, ValidationError
from database.database import db
from database.models import TransactionType

transaction_type = Blueprint('transaction_type', __name__)

class TransactionTypeSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.String(required=True)
    
@transaction_type.route('/transaction_types', methods=['GET'])
def get_transaction_types():
    types = TransactionType.query.all()
    types_list = TransactionTypeSchema(many=True).dump(types)
    return jsonify(types_list), 200

@transaction_type.route('/transaction_types', methods=['POST'])
def create_transaction_type():
    req = request.get_json()
    if not req:
        return jsonify({"error": "No data provided"}), 400

    schema = TransactionTypeSchema()
    try:
        validated_data = schema.load(req)
    except ValidationError as err:
        return jsonify(err.messages), 400

    transaction_type = TransactionType(name=validated_data['name'])
    
    try:
        db.session.add(transaction_type)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

    return jsonify(TransactionTypeSchema().dump(transaction_type)), 201

@transaction_type.route('/transaction_types/<int:transaction_type_id>', methods=['PUT'])
def update_transaction_type(transaction_type_id):
    return jsonify({"message": "Endpoint not implemented yet"}), 501

@transaction_type.route('/transaction_types/<int:transaction_type_id>', methods=['DELETE'])
def delete_transaction_type(transaction_type_id):
    return jsonify({"message": "Endpoint not implemented yet"}), 501