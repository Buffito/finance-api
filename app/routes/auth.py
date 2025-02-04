from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt, JWTManager
from app.models import User,RevokedToken
from datetime import timedelta
from app import db

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
    
    if not user or not check_password_hash(user.password, password):
        return jsonify({"message": "Invalid credentials"}), 401

    access_token = create_access_token(identity=user.id, expires_delta=timedelta(minutes=10))
    return jsonify({"message": "Login successful", "access_token": access_token}), 200

@auth.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    jti = get_jwt()['jti']
    revoked_token = RevokedToken(jti=jti)
    db.session.add(revoked_token)
    db.session.commit()
    return jsonify({"message": "Logout successful"}), 200