from flask import Flask
from flask import request
from vertexai.preview.language_models import TextGenerationModel
import os
import random

MODEL = "text-bison"
TOPIC = "History"
NUM_Q = 5
NUM_A = 4
MAX_TOKENS = 1024
TOP_P = 0.8
TOP_K = 40
DIFF = "medium"
LANG = "English"
TEMP = 0.5

PROMPT = """ 
Generate a quiz according to the following specifications:

- topic: {topic}
- num_q: {num_q}
- num_a: {num_a}
- diff:  {diff}
- lang:  {lang}
"""

app = Flask(__name__)  # Create a Flask object.
PORT = os.environ.get("PORT")  # Get PORT setting from environment.


def check(args, name, default):
    if name in args:
        return args[name]
    return default


# The app.route decorator routes any GET requests sent to the /generate
# path to this function, which responds with "Generating:” followed by
# the body of the request.
@app.route("/", methods=["GET"])
# This function generates a quiz using Vertex AI.
def generate():
    args = request.args.to_dict()
    topic = check(args, "topic", TOPIC)
    num_q = check(args, "num_q", NUM_Q)
    num_a = check(args, "num_a", NUM_A)
    diff = check(args, "diff", DIFF)
    lang = check(args, "lang", LANG)
    temp = check(args, "temp", TEMP)

    prompt = PROMPT.format(topic=topic, num_q=num_q, num_a=num_a, diff=diff, lang=lang)
    model = TextGenerationModel.from_pretrained(MODEL)
    response = model.predict(
        prompt,
        temperature=temp,
        max_output_tokens=MAX_TOKENS,
        top_k=TOP_K,
        top_p=TOP_P,
    )
    return response.text


# This code ensures that your Flask app is started and listens for
# incoming connections on the local interface and port 8080.
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
