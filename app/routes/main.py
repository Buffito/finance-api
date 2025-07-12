from flask import Blueprint, jsonify
from flasgger import swag_from
from .swagger_specs import index_spec

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
@swag_from(index_spec)
def index():   
    return jsonify({"message": "API is running"}), 200