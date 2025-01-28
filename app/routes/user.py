from flask import Blueprint, request
from app.services import UserService

user = Blueprint('user', __name__)

@user.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    result = UserService.create_user(data)
    return result