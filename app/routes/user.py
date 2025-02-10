from flask import Blueprint, request
from app.services import UserService

user = Blueprint('user', __name__)

@user.route('/register', methods=['POST'])
def create_user():
    data = request.get_json()
    return UserService.create_user(data)