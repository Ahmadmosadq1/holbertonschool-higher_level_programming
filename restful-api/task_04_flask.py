from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# In-memory storage for users
users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}
}

@app.route("/")
def home():
    """Home page endpoint"""
    return "Welcome to the Flask API!"

@app.route("/data")
def get_users():
    """Returns a list of all usernames stored in the API"""
    names = list(users.keys())
    return jsonify(names)

@app.route("/status")
def get_status():
    """Returns the status of the API"""
    return "OK"

@app.route("/users/<username>")
def find_users(username):
    """Returns the full object corresponding to the provided username"""
    user = users.get(username)
    if user is None:
        abort(404, description="User not found")
    return jsonify(user)

@app.route("/add_user", methods=["POST"])
def add_user():
    """Handles POST requests to add new users"""
    data = request.get_json()
    if not data:
        abort(400, description="Missing JSON body")

    username = data.get("username")
    if not username:
        abort(400, description="username is required")

    if username in users:
        abort(409, description="User already exists")

    # Store the new user object under its username
    users[username] = data

    # Return a confirmation message with the added user's data
    return jsonify({
        "message": "User added successfully",
        "user": data
    }), 201

if __name__ == "__main__":
    app.run()