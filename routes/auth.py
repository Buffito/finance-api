from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
from database.models import User

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and check_password_hash(user.password, data['password']):
        # Generate and return token
        token = "generated_token"
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"message": "Invalid credentials"}), 401

@auth.route('/logout', methods=['POST'])
def logout():
    # Invalidate the token here
    return jsonify({"message": "Logout successful"}), 200