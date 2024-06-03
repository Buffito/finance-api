from flask import Blueprint, jsonify
#from models import User
#from app import db

main = Blueprint('main', __name__)

@main.route("/", methods=["GET"])
def index():
    return 'hello'

#@main.route("/users", methods=["GET"])
#def user_list():
#    users = db.session.execute(db.select(User).order_by(User.username)).scalars()
#    return jsonify(users)