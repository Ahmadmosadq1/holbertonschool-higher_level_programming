from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# In-memory store
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28},
    "bob":  {"username": "bob",  "name": "Bob",  "age": 25},
}

@app.route("/")
def home():
    """Home page."""
    return "Welcome to the Flask API!"

@app.route("/data")
def get_users():
    """
    Return a JSON list of all usernames.
    """
    names = list(users.keys())
    return jsonify(names)

@app.route("/status")
def get_status():
    """
    Health check endpoint.
    """
    return "OK", 200

@app.route("/users/<username>")
def get_user(username):
    """
    Return the full user object for the given username,
    or 404 if not found.
    """
    user = users.get(username)
    if not user:
        abort(404, description="User not found")
    return jsonify(user)

@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Accept a JSON body like:
      { "username":"john","name":"John","age":30,"city":"New York" }
    Add it to `users` under its "username", and return a 201 with confirmation.
    """
    data = request.get_json()
    if not data:
        abort(400, description="Missing JSON body")

    username = data.get("username")
    if not username:
        abort(400, description="username is required")

    if username in users:
        abort(409, description="User already exists")

    users[username] = data

    return jsonify({
        "message": "User added successfully",
        "user": data
    }), 201

if __name__ == "__main__":
    # bind to all interfaces if you need external access:
    # app.run(host="0.0.0.0", port=5000)
    app.run(port=5000)
