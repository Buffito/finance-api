from flask import Blueprint, request, jsonify
from marshmallow import Schema, fields, ValidationError
from werkzeug.security import generate_password_hash
from database.database import db
from database.models import User

user = Blueprint('user', __name__)

class UserSchema(Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)

@user.route('/users', methods=['GET'])
def get_users():
    return jsonify({"message": "Endpoint not implemented yet"}), 501

@user.route('/users', methods=['POST'])
def create_user():
    req = request.get_json()
    schema = UserSchema()
    try:
        validated_data = schema.load(req)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    hashed_password = generate_password_hash(validated_data['password'])
    new_user = User(username=validated_data['username'], password=hashed_password)
    
    try:
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400
    
    return jsonify({"message": "User created successfully!"}), 200
    
@user.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    return jsonify({"message": "Endpoint not implemented yet"}), 501

@user.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return jsonify({"message": "Endpoint not implemented yet"}), 501