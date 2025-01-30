# TODO List 
# Date: 28/1/2025

## General
- [x] Add a TODO.md file
- [x] Refactor the $h!+ out of the existing code
- [x] Create specific routes
- [ ] Add authentication (JWT)
- [x] Add user model and routes
- [ ] Secure API endpoints
- [x] Remove not implemented endpoints for cleaner, more readable code 
- [x] Should make transaction types static since more won't be added
  - [x] Add initial transaction types to the database
- [X] Restructure project to comply with Flask best practices
 - [x] Have separate directories for routes, models, schemas, and services
 - [x] Move schemas to a separate schemas.py file
 - [x] Create a config.py file for configuration settings
 - [x] Use a run.py file as the entry point for the application and remove app.py
 - [x] Remove business logic and CRUD operations from route files
  - [X] Place above into service files

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
  - [x] Delete routes
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
  - [x] Transaction routes
  - [x] Transaction type routes (will be deleted)
    - [x] Deleted
  - [ ] Authentication routes
  - [x] User routes
