from app.models import Transaction, User
from app.schemas import TransactionSchema, UserSchema

class TestService:
    @staticmethod
    def get_all_transactions():
        transactions = Transaction.query.all()
        return TransactionSchema(many=True).dump(transactions)
    
    @staticmethod
    def get_all_users():
        users = User.query.all()
        return UserSchema(many=True).dump(users)