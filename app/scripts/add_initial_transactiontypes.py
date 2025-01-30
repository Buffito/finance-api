import sys
import os

# Add the root directory of the project to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from app import create_app, db
from app.models import TransactionType

def add_initial_transaction_types():
    initial_types = [
        {"name": "Income"},
        {"name": "Expense"}
    ]

    for type_data in initial_types:
        transaction_type = TransactionType(**type_data)
        db.session.add(transaction_type)

    db.session.commit()

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        add_initial_transaction_types()