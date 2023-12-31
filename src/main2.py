from flask import Flask
from flask import request
import os
import random

app = Flask(__name__)  # Create a Flask object.
PORT = os.environ.get("PORT")  # Get PORT setting from environment.


# The app.route decorator routes any GET requests sent to the /generate
# path to this function, which responds with "Generating:” followed by
# the body of the request.
@app.route("/", methods=["GET"])
def generate():
    args = request.args.to_dict()
    html = f"<h1>Generating:</h1><br>{args}"
    return html


# This code ensures that your Flask app is started and listens for
# incoming connections on the local interface and port 8080.
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
