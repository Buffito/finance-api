# Finance API

This is an API developed in Python-Flask. It supports user authentication using JWT tokens and provides endpoints for creating, retrieving, and managing transactions. It's purpose was for me 
to learn more about APIs and create something useful in the process.

## Features

- User authentication with JWT tokens
- CRUD operations for transactions
- Data validation with Marshmallow schemas

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/Buffito/finance-api.git
    cd finance-api
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

2. Use an API client like Postman to interact with the API, or open [http://localhost:5000/apidocs](http://localhost:5000/apidocs) in your browser to view and interact with the API documentation via

## License

This project is licensed under the MIT License.