from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, JWTManager
from app.models import User
from datetime import timedelta

auth = Blueprint('auth', __name__)

jwt = JWTManager()

@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity=user.id, expires_delta=timedelta(minutes=10))
        return jsonify({"message": "Login successful", "access_token": access_token}), 200
    return jsonify({"message": "Invalid credentials"}), 401

@auth.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    # Invalidate the token here
    return jsonify({"message": "Logout successful"}), 200