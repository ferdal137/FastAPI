# Movie Review Web API using FastAPI

## Description

Welcome to the Movie Review Web API repository! This project is developed using FastAPI, a modern and efficient web framework for building APIs with Python. The API serves as the backend for a movie review website, allowing both authenticated users and anonymous users to perform various operations related to movie reviews. The project incorporates features such as cookie management, JSON responses, input validations, HTTP verbs, OAuth2 authentication, and more.

## Features

1. **User Authentication:**
   - Support for both authenticated and anonymous users.
   - OAuth2 authentication for enhanced security.

2. **CRUD Operations:**
   - Create: Authenticated users can create new movie reviews.
   - Read: Users (authenticated or anonymous) can retrieve movie reviews.
   - Update: Authenticated users can update their own movie reviews.
   - Delete: Authenticated users can delete their own movie reviews.

3. **Cookie Management:**
   - Efficient handling of cookies for user session management.
   - Secure storage of session-related data.

4. **JSON Responses:**
   - Responses are formatted in JSON for easy consumption by frontend applications.

5. **Input Validation:**
   - Comprehensive validation of input data to ensure data integrity.

6. **HTTP Verbs:**
   - Proper utilization of HTTP verbs (GET, POST, PUT, DELETE) for appropriate operations.

## Used Modules

The following Python modules are used in this project:

- **FastAPI:** The main web framework used for building the API endpoints.
- **uvicorn:** ASGI server used to run the FastAPI application.
- **peewee:** A simple and expressive SQL database toolkit.
- **mysqlclient:** MySQL database connector for Python.
- **requests:** Library for making HTTP requests to external services.
