index_spec = {
    "tags": ["Default"],
    "summary": "Check if API is running",
    "responses": {
        200: {
            "description": "API is running",
            "schema": {
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string",
                        "example": "API is running"
                    }
                }
            }
        }
    }
}

register_user_spec = {
    "tags": ["User"],
    "summary": "Register a new user",
    "description": "Creates a new user account.",
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "username": {"type": "string", "example": "johndoe"},
                    "password": {"type": "string", "example": "secret123"}
                },
                "required": ["username", "password"]
            }
        }
    ],
    "responses": {
        201: {
            "description": "User created successfully"
        },
        400: {
            "description": "Invalid input"
        }
    }
}

login_spec = {
    "tags": ["Auth"],
    "summary": "User login",
    "description": "Authenticate user and return a JWT access token.",
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "username": {"type": "string", "example": "johndoe"},
                    "password": {"type": "string", "example": "secret123"}
                },
                "required": ["username", "password"]
            }
        }
    ],
    "responses": {
        200: {
            "description": "Login successful",
            "schema": {
                "type": "object",
                "properties": {
                    "access_token": {"type": "string"},
                    "id": {"type": "integer"}
                }
            }
        },
        400: {"description": "Missing username or password"},
        401: {"description": "Invalid credentials"}
    }
}

refresh_spec = {
    "tags": ["Auth"],
    "summary": "Refresh JWT token",
    "description": "Refresh and return a new JWT access token.",
    "security": [{"Bearer": []}],
    "responses": {
        200: {
            "description": "Token refreshed",
            "schema": {
                "type": "object",
                "properties": {
                    "access_token": {"type": "string"}
                }
            }
        }
    }
}

create_transaction_spec = {
    "tags": ["Transaction"],
    "summary": "Create a new transaction",
    "description": "Create a new transaction for a user.",
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "type_id": {"type": "integer", "example": 1},
                    "amount": {"type": "number", "format": "float", "example": 100.0},
                    "at_date": {"type": "string", "format": "date", "example": "2024-01-01"},
                    "user_id": {"type": "integer", "example": "1"}
                },
                "required": ["type_id","amount", "at_date", "user_id"]
            }
        }
    ],
    "security": [{"Bearer": []}],
    "responses": {
        201: {"description": "Transaction created"},
        400: {"description": "Invalid input"}
    }
}

get_transactions_by_user_id_spec = {
    "tags": ["Transaction"],
    "summary": "Get all transactions for a user",
    "description": "Retrieve all transactions for a specific user by user ID.",
    "parameters": [
        {
            "name": "user_id",
            "in": "path",
            "type": "integer",
            "required": True,
            "description": "User ID"
        }
    ],
    "security": [{"Bearer": []}],
    "responses": {
        200: {
            "description": "List of transactions",
            "schema": {
                "type": "array",
                "items": {"type": "object"}
            }
        }
    }
}