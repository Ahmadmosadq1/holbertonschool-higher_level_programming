from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt_identity, get_jwt
)

app = Flask(__name__)

# Secret key for JWT; in real deployments, load from secure config/environment
app.config['JWT_SECRET_KEY'] = 'your-very-strong-secret-key'

# HTTP Basic Auth setup
auth = HTTPBasicAuth()

# JWT setup
jwt = JWTManager(app)

# In-memory user store with hashed passwords and roles
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),  # hashed
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),  # hashed
        "role": "admin"
    }
}

#
# -------- Basic Authentication Handlers --------
#

@auth.verify_password
def verify_password(username, password):
    """
    Verify Basic Auth credentials: check username exists and password matches.
    """
    user = users.get(username)
    if not user:
        return False
    return check_password_hash(user['password'], password)

@auth.error_handler
def basic_auth_error():
    """
    Return JSON 401 for any Basic Auth failure.
    """
    return jsonify(error="Unauthorized access"), 401

@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """
    A GET endpoint protected by Basic Auth.
    Returns plain-text message on success.
    """
    return "Basic Auth: Access Granted", 200

#
# -------- JWT Authentication Handlers --------
#

# These handlers ensure any JWT error returns JSON with 401 status,
# matching the requirement that missing/invalid/expired tokens all yield 401.

@jwt.unauthorized_loader
def handle_missing_token(err_msg):
    """
    Called when no JWT is present in a protected endpoint.
    """
    return jsonify(error="Missing or invalid token"), 401

@jwt.invalid_token_loader
def handle_invalid_token(err_msg):
    """
    Called when JWT is malformed or invalid.
    """
    return jsonify(error="Invalid token"), 401

@jwt.expired_token_loader
def handle_expired_token(jwt_header, jwt_payload):
    """
    Called when a valid JWT is present but expired.
    """
    return jsonify(error="Token has expired"), 401

@jwt.revoked_token_loader
def handle_revoked_token(jwt_header, jwt_payload):
    """
    If you implement token revocation, this fires when token is revoked.
    """
    return jsonify(error="Token has been revoked"), 401

@jwt.needs_fresh_token_loader
def handle_fresh_token_required(jwt_header, jwt_payload):
    """
    Called when a fresh token is required but a non-fresh one is provided.
    """
    return jsonify(error="Fresh token required"), 401

#
# -------- Authentication Routes --------
#

@app.route('/login', methods=['POST'])
def login():
    """
    Login endpoint for JWT. Expects JSON: {"username": "...", "password": "..."}.
    On valid credentials, returns {"access_token": "<JWT_TOKEN>"}.
    On missing/invalid credentials, returns 401 with JSON error.
    """
    data = request.get_json()
    # If no JSON at all or missing fields
    if not data or 'username' not in data or 'password' not in data:
        return jsonify(error="Missing username or password"), 401

    username = data['username']
    password = data['password']
    user = users.get(username)
    if not user or not check_password_hash(user['password'], password):
        return jsonify(error="Bad credentials"), 401

    # Include role in JWT claims so we can check it later
    additional_claims = {"role": user['role']}
    access_token = create_access_token(identity=username, additional_claims=additional_claims)
    return jsonify(access_token=access_token), 200

@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """
    A GET endpoint protected by JWT.
    Returns plain-text message if token is valid.
    """
    return "JWT Auth: Access Granted", 200

@app.route('/admin-only')
@jwt_required()
def admin_only():
    """
    A GET endpoint accessible only to users with role "admin".
    If JWT is missing/invalid → 401 via handlers above.
    If user is not admin → 403 JSON {"error": "Admin access required"}.
    If admin → plain-text "Admin Access: Granted".
    """
    # Retrieve role from JWT claims
    claims = get_jwt()
    role = claims.get("role", None)
    if role != "admin":
        return jsonify(error="Admin access required"), 403
    return "Admin Access: Granted", 200

#
# -------- Main --------
#

if __name__ == "__main__":
    # Run on port 5000, accessible on localhost. For external access, use host="0.0.0.0"
    app.run(port=5000)
