from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, JWTManager
from app.models import User
from datetime import timedelta

auth = Blueprint('auth', __name__)

jwt = JWTManager()

@auth.route('/login', methods=['POST'])
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
        identity = str(user.id)+"_"+str(user.username)
        access_token = create_access_token(identity=str(identity), expires_delta=timedelta(minutes=10))
        return jsonify({"message": "Login successful", "access_token": access_token, "id": user.id}), 200

    return jsonify({"message": "Invalid credentials"}), 401