from flask import Blueprint, request, jsonify
from app.services import UserService

user = Blueprint('user', __name__)

@user.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    return UserService.create_user(data)

# For testing purposes
@user.route('/users', methods=['GET'])
def get_users():
    users = UserService.get_all()
    return jsonify(users), 200