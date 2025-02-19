# RESTful API Implementation Guide

## Project Structure
```
restful-api/
├── task_02_requests.py    # API consumption with requests
├── task_03_http_server.py # Basic HTTP server implementation
├── task_04_flask.py       # Flask API implementation
├── task_05_basic_security.py # Secured API with authentication
└── main_02_requests.py    # Test file for task 02
```

## 1. HTTP/HTTPS Basics (0-http_basics.md)
- Explains the fundamental differences between HTTP and HTTPS
- Details common HTTP methods (GET, POST, PUT, DELETE)
- Lists important status codes (200, 201, 400, 404, 500)
- Demonstrates request/response structure
- Covers security implications

## 2. API Consumption with curl (1-curl_basics.md)
- Shows how to use curl for API testing
- Covers basic GET and POST requests
- Demonstrates header manipulation
- Includes common curl options and examples
- Provides expected output examples

## 3. API Consumption with Python (task_02_requests.py)
```python
# Key features:
- Uses requests library for HTTP requests
- Implements GET requests to JSONPlaceholder API
- Processes JSON responses
- Saves data to CSV format
- Handles status codes and errors
```

## 4. Basic HTTP Server (task_03_http_server.py)
```python
# Implementation details:
- Uses Python's built-in http.server
- Handles different routes (/. /data, /info)
- Returns JSON responses
- Includes error handling
- Simple and lightweight
```

## 5. Flask API (task_04_flask.py)
```python
# Features:
- RESTful API implementation
- In-memory user storage
- CRUD operations
- JSON response formatting
- Status code handling
```

## 6. Secured API (task_05_basic_security.py)
```python
# Security features:
- Basic Authentication
- JWT token authentication
- Role-based access control
- Password hashing
- Protected routes
```

## Setting Up Each Component

### 1. Basic HTTP Server
```bash
# Start the server
python3 task_03_http_server.py
# Server runs on port 8000
```

### 2. Flask API
```bash
# Install Flask
pip install flask

# Run the server
flask --app task_04_flask.py run
# Server runs on port 5000
```

### 3. Secured API
```bash
# Install requirements
pip install flask flask-httpauth flask-jwt-extended

# Run the server
flask --app task_05_basic_security.py run
```

## Testing the APIs

### Basic HTTP Server
```bash
curl http://localhost:8000/
curl http://localhost:8000/data
curl http://localhost:8000/info
```

### Flask API
```bash
curl http://localhost:5000/
curl http://localhost:5000/data
curl http://localhost:5000/users/jane
curl -X POST -H "Content-Type: application/json" \
     -d '{"username":"alice","name":"Alice","age":25,"city":"SF"}' \
     http://localhost:5000/add_user
```

### Secured API
```bash
# Basic auth
curl -u user1:password http://localhost:5000/basic-protected

# Get JWT token
curl -X POST -H "Content-Type: application/json" \
     -d '{"username":"user1","password":"password"}' \
     http://localhost:5000/login

# Use JWT token
curl -H "Authorization: Bearer <token>" \
     http://localhost:5000/jwt-protected
```

## Best Practices Implemented

1. **Error Handling**
   - Consistent error responses
   - Proper status codes
   - Informative error messages

2. **Security**
   - Password hashing
   - Token-based authentication
   - Role-based access control
   - Header validation

3. **Code Organization**
   - Modular design
   - Clear function names
   - Docstrings
   - Separation of concerns

4. **API Design**
   - RESTful principles
   - Clear endpoints
   - Consistent response format
   - Proper HTTP methods

## Development Tips

1. Always test endpoints with curl or Postman
2. Use proper error handling
3. Implement security from the start
4. Document your API endpoints
5. Use environment variables for sensitive data
6. Follow REST conventions
7. Include proper status codes
8. Validate input data
9. Handle edge cases
10. Write clear documentation

## Production Considerations

1. Use HTTPS in production
2. Change secret keys
3. Implement rate limiting
4. Add proper logging
5. Use a production-grade server
6. Implement proper database storage
7. Add monitoring
8. Regular security audits
9. Backup strategies
10. Scalability planning