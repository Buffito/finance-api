import os
import sys

# Add the root directory of the project to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from app import create_app, db
from app.models import Transaction, User  

def clear_db_except_transaction_types():
    models_to_clear = [Transaction, User]  

    for model in models_to_clear:
        db.session.query(model).delete()

    db.session.commit()

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        clear_db_except_transaction_types()