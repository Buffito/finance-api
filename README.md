# Flask Transaction API

This is a Flask-based API for managing transactions. The API supports user authentication using JWT tokens and provides endpoints for creating, retrieving, and managing transactions.

## Features

- User authentication with JWT tokens
- CRUD operations for transactions
- Token revocation for secure logout
- Data validation with Marshmallow schemas

## Requirements

- Python 3.7+
- Flask
- Flask-JWT-Extended
- Flask-SQLAlchemy
- Flask-Migrate
- Marshmallow
- python-dotenv

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/Buffito/flask-transaction-api.git
    cd flask-transaction-api
    ```

2. Create and activate a virtual environment:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Set up the environment variables:

    Create a [.env](http://_vscodecontentref_/0) file in the root directory of the project and add the following:

    ```properties
    SQLALCHEMY_DATABASE_URI="sqlite:///transactions.db"
    SECRET_KEY="your-secret-key"
    JWT_SECRET_KEY="your-jwt-secret-key"
    ```

5. Initialize the database:

    ```sh
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade
    ```

6. Add initial transaction types:

    ```sh
    python app/scripts/add_initial_transactiontypes.py
    ```

## Usage

1. Run the Flask application:

    ```sh
    flask run
    ```

2. Use an API client like Postman to interact with the API.

## API Endpoints

### Authentication

- **POST /login**: Authenticate a user and receive a JWT token.
    - Request body: `{ "username": "user1", "password": "password123" }`
    - Response: `{ "access_token": "your.jwt.token.here" }`

- **POST /logout**: Invalidate the current JWT token.
    - Headers: `Authorization: Bearer your.jwt.token.here`
    - Response: `{ "message": "Logout successful" }`

### Transactions

- **GET /transactions/user/<user_id>**: Retrieve all transactions for a specific user.
    - Headers: `Authorization: Bearer your.jwt.token.here`
    - Response: `[ { "id": 1, "transaction_type": { "id": 1, "name": "Income" }, "amount": 100.0, "at_date": "2023-10-10", "user_id": 1 }, ... ]`

- **POST /transactions**: Create a new transaction.
    - Headers: `Authorization: Bearer your.jwt.token.here`
    - Request body: `{ "transaction_type": { "id": 1 }, "amount": 100.0, "user_id": 1 }`
    - Response: `{ "id": 1, "transaction_type": { "id": 1, "name": "Income" }, "amount": 100.0, "at_date": "2023-10-10", "user_id": 1 }`

## License

This project is licensed under the MIT License.