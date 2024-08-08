from flask import Blueprint, request
from database.database import db
from database.models import Transaction
from database.models import TransactionType
import json
main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
def index():
    return 'success', 200


@main.route('/transactions', methods=['GET'])
def transaction_list():
    result = db.session.execute(
        db.select(Transaction), execution_options={"prebuffer_rows": True}
    )
    transactions = result.scalars().all()
    
    return 'success', 200


@main.route('/transactiontypes', methods=['GET'])
def transaction_types_list():
    result = db.session.execute(
        db.select(TransactionType), execution_options={"prebuffer_rows": True}
    )
    transaction_types = result.scalars().all()

    json_str = '['
    for tt in transaction_types:
        json_str = json_str + '{ \"id\":' + str(tt.id) + ', \"description\": \"' + tt.description + '\"},'
    json_str = json_str + ']'

    return json_str, 200


# transactiontypes/add/?descr=Income
@main.route('/transactiontypes/add/', methods=['GET', 'POST'])
def add_transaction_types():
    code = 200
    msg = 'success'
    if request.method == 'POST':
        data = request.args.to_dict()
        transaction_type = TransactionType()
        transaction_type.description = data['descr']
        try:
            db.session.add(transaction_type)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            code = 404
            msg = 'failure'
        db.session.flush()  # for resetting non-commited .add()
        db.session.close()
        
    return msg,code

# https://auth0.com/blog/developing-restful-apis-with-python-and-flask/ get some inspiration for some modeling
