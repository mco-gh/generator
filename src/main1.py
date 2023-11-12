from flask import Flask
from flask import request
import os
import random

app = Flask(__name__)  # Create a Flask object.
PORT = os.environ.get("PORT")  # Get PORT setting from the environment.


# The app.route decorator routes any GET requests sent to the root path
# to this function, which responds with a "Hello world!" HTML document.
@app.route("/", methods=["GET"])
def say_hello():
    html = "<h1>Hello world!</h1>"
    return html


# This code ensures that your Flask app is started and listens for
# incoming connections on the local interface and port 8080.
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
