#!/usr/bin/python3
"""Flask API with Basic and JWT Authentication"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, get_jwt_identity,
    jwt_required
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config['JWT_SECRET_KEY'] = 'super-secret-key'  # Change in production!
jwt = JWTManager(app)

# User database with hashed passwords
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """Verify basic auth credentials"""
    if username in users and check_password_hash(
            users[username]["password"], password):
        return username
    return None


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """Basic auth protected endpoint"""
    return jsonify({"message": "Basic Auth: Access Granted"})


@app.route('/login', methods=['POST'])
def login():
    """Login endpoint to get JWT token"""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 401

    if username not in users or not check_password_hash(
            users[username]["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(
        identity={"username": username, "role": users[username]["role"]})
    return jsonify({"access_token": access_token})


@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """JWT protected endpoint"""
    return jsonify({"message": "JWT Auth: Access Granted"})


@app.route('/admin-only')
@jwt_required()
def admin_only():
    """Admin-only endpoint"""
    current_user = get_jwt_identity()
    if current_user.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return jsonify({"message": "Admin Access: Granted"})


# Error handlers
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handle missing JWT token"""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handle invalid JWT token"""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(header, payload):
    """Handle expired JWT token"""
    return jsonify({"error": "Token has expired"}), 401


@auth.error_handler
def auth_error(status):
    """Handle basic auth errors"""
    return jsonify({"error": "Unauthorized"}), 401


if __name__ == '__main__':
    app.run(debug=True)
