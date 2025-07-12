from flask import Blueprint, request
from app.services import UserService
from flasgger import swag_from
from .swagger_specs import register_user_spec

user = Blueprint('user', __name__)

@user.route('/register', methods=['POST'])
@swag_from(register_user_spec)
def create_user():
    data = request.get_json()
    return UserService.create_user(data)