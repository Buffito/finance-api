# TODO List 
# Date: 27/1/2025

## General
- [x] Add a TODO.md file
- [x] Refactor the $h!+ out of the existing code
- [x] Create specific routes
- [ ] Add authentication (JWT)
- [x] Add user model and routes
- [ ] Secure API endpoints
- [ ] Remove not implemented endpoints for cleaner, more readable code (?)
- [ ] Create schema.py to store schemas and remove them from routes
- [ ] Should make transaction types static since more won't be added
  - [ ] Add initial transaction types to the database
- [ ] Change transaction types to category (ex. "Income", "Expense")
- [ ] Restructure project to comply with Flask best practices

## Routes
- [x] Main route
  - [x] Add a simple main route
- [ ] Transaction routes
  - [x] Write basic endpoints
  - [x] Get all transaction types and create transaction type implemented - others not needed
  - [x] Implement all endpoints fully
  - [x] Added schema for data validation
  - [ ] Add user related endpoints - modify existing ones
- [x] Transaction type routes
  - [x] Write basic endpoints
  - [x] Get all transaction types and create transaction type implemented - others not needed
  - [x] Implement all endpoints fully
  - [x] Added schema for data validation
  - [ ] Delete route
- [ ] User routes
  - [x] Write basic endpoints
  - [x] Added schema for data validation
  - [x] Implement create user - others not needed for now
- [ ] Authentication routes
  - [x] Added login endpoint
  - [ ] Implement login endpoint fully and correctly
  - [ ] Implement logout endpoint fully and correctly

## Testing
- [ ] Test the API with Postman
  - [x] Main route
  - [ ] Transaction routes
  - [x] Transaction type routes (will be deleted)
  - [ ] Authentication routes
  - [ ] User routes
