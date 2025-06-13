from flask import Flask, request, jsonify, abort

app = Flask(__name__)
"""app starts the flask applicaation"""

"""home page"""
@app.route("/")
def home():
    return "Welcome to the Flask API!"

users = {}
"""In-memory store of users:
Originally, examples were:
{
    "jane": {"username": "jane", "name": "Jane", "age": 28},
    "bob":  {"username": "bob",  "name": "Bob",  "age": 25},
    # …etc…
}
But start empty for this API so GET /data returns [] initially.
"""

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
    if not user:
        return jsonify(error="User not found"), 404
    return jsonify(user)

@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Original comments:
    # no JSON at all
    # username field is required
    # avoid overwriting existing user
    # store the new user object under its username
    # return a confirmation with the added data
    """
    data = request.get_json()
    if data is None:
        """no JSON at all"""
        return jsonify(error="Missing JSON body"), 400

    username = data.get("username")
    if not username:
        """username field is required"""
        return jsonify(error="username is required"), 400

    if username in users:
        """avoid overwriting existing user"""
        return jsonify(error="User already exists"), 409

    """store the new user object under its username"""
    users[username] = data

    """return a confirmation with the added data"""
    return jsonify(message="User added successfully", user=data), 201

if __name__ == "__main__":
    """Run the Flask development server on port 5000."""
    app.run(port=5000)
