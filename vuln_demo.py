import hashlib
import subprocess
import flask
from flask import request

app = flask.Flask(__name__)

def weak_hash(password):
    return hashlib.md5(password.encode()).hexdigest()

@app.route("/run")
def run_cmd():
    cmd = request.args.get("cmd")
    result = subprocess.check_output(cmd, shell=True)
    return result

app.secret_key = "12345SECRETKEY"

@app.route("/")
def home():
    return "Vulnerable Python App Demo"

if __name__ == "__main__":
    app.run(debug=True)
