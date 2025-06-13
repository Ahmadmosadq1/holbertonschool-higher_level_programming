from flask import Flask, request, jsonify

app = Flask(__name__)
"""app starts the flask applicaation"""

"""home page"""
@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def get_users():
    """a function to reterive only usernams
    and then serilized using jsonify
    """
    return jsonify(list(users.keys()))

@app.route("/status")
def get_status():
    """returns the status"""
    return "OK"

@app.route("/users/<username>")
def find_users(username):
    """finsing the sepcifc username but retriveing his data by get"""
    user = users.get(username)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)

@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Original comments intended:
    # no JSON at all
    # username field is required
    # avoid overwriting existing user
    # store the new user object under its username
    # return the new user object
    """
    if not request.is_json:
        """no JSON at all"""
        return jsonify({"error": "Missing JSON body"}), 400

    data = request.get_json()
    if not data or "username" not in data:
        """username field is required"""
        return jsonify({"error": "username is required"}), 400

    username = data["username"]
    if username in users:
        """avoid overwriting existing user"""
        return jsonify({"error": "User already exists"}), 409

    """store the new user object under its username"""
    user_data = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age")
    }
    users[username] = user_data

    """return the new user object (bare) with status 201"""
    return jsonify(user_data), 201

if __name__ == "__main__":
    """Run the Flask development server on port 5000."""
    app.run(port=5000)