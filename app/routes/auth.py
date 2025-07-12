from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, JWTManager, get_jwt_identity
from app.models import User
from flasgger import swag_from
from .swagger_specs import login_spec, refresh_spec

auth = Blueprint('auth', __name__)

jwt = JWTManager()

@auth.route('/login', methods=['POST'])
@swag_from(login_spec)
def login():
    data = request.get_json()
    if 'username' not in data.keys():
        return jsonify({"message": "Missing username"}), 400
    if 'password' not in data.keys():
        return jsonify({"message": "Missing password"}), 400
    
    username = data['username'].strip()
    password = data['password'].strip()
    
    user = User.query.filter_by(username=username).first()
    
    if user and User.check_password(user.password, password):
        access_token = create_access_token(identity=str(user), fresh=True)
        return jsonify({"access_token": access_token, "id": user.id}), 200

    return jsonify({"message": "Invalid credentials"}), 401

@auth.route('/refresh', methods=['POST'])
@jwt_required()
@swag_from(refresh_spec)
def refresh():    
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity, fresh=False)
    return jsonify(access_token=access_token)