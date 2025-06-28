
from flask import Flask
import os

app = Flask(__name__)
GREETING = os.environ.get("GREETING", "Hello from Flask on Kubernetes!")

@app.route("/")
def hello():
    return f"<h1>{GREETING}</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
