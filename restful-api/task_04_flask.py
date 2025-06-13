from flask import Flask
from flask import jsonify
import requests

app = Flask(__name__)
"""app starts the flask applicaation"""

"""home page"""
@app.route("/")
def home():
    return "Welcome to the Flask API!"
@app.route("/data")
def get_users():
    """a function to reterive only usernams
    and then serilized using jsonfy
    """
    names = list(users.keys())
    return jsonify(names)

@app.route("/status")
def get_status():
    """returns the status"""
    return "OK", 200

@app.route("/users/<username>")
def find_users(username):
    """finsing the sepcifc username but retriveing his name by get"""
    user = users.get(username)
    return jsonify(user)
@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    if not data:
        # no JSON at all
        abort(400, description="Missing JSON body")

    username = data.get("username")
    if not username:
        # username field is required
        abort(400, description="username is required")

    if username in users:
        # avoid overwriting existing user
        abort(409, description="User already exists")

    # store the new user object under its username
    users[username] = data

    # return a confirmation with the added data
    return jsonify({
        "message": "User added successfully",
        "user": data
    }), 201


if __name__ == "__main__": 
    app.run()
