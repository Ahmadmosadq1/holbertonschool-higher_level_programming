from flask import Flask, request, jsonify

app = Flask(__name__)

# start with an empty store
users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def get_usernames():
    # Return a JSON array of all the usernames (the dict keys)
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    return "OK", 200

@app.route("/users/<username>")
def get_user(username):
    # If the user isn't in our dict, return a JSON 404
    if username not in users:
        return jsonify(error="User not found"), 404
    # Otherwise return the full user object
    return jsonify(users[username])

@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    if not data:
        return jsonify(error="Missing JSON body"), 400

    username = data.get("username")
    if not username:
        return jsonify(error="username is required"), 400

    if username in users:
        return jsonify(error="User already exists"), 409

    # store the new user under its username
    users[username] = data

    # return exactly the new user object, with 201 Created
    return jsonify(data), 201

if __name__ == "__main__":
    # tests hit http://127.0.0.1:5000 by default
    app.run(port=5000)
