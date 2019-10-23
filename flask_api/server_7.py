#!/usr/bin/python3

from flask import Flask
from flask import make_response
from flask import request
from flask import render_template
from flask import url_for
from flask import redirect
from flask import escape
from flask import session
from flask import jsonify
app = Flask(__name__)
app.secret_key = "chaos is a ladder"
@app.route("/")
def home():
    if "username" in session:
        username = session["username"]

        return "logged in as " + username + "<br> <a href = '/logout'>click here to logout</a>"
    return "You are not logged in <br> <a href = '/login'>Click here to login</a></br>"

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        session["username"] = request.form.get("username")
        return redirect(url_for("home"))
    return """
    <form action = "" method = "POST">
    <p><input type = "text" name ="username"></p>
    <p><input type = "submit" value="submit"></p> 
    </form>
    """

@app.route("/logout")
def logout():
    session.pop("username",None)
    return redirect(url_for("home"))
@app.route("/jsondata")
def jsondata():
    if session.get("username"):
        return jsonify({"apple":"192.168.23.1"})
    else:
        return redirect(url_for("login"))



if __name__ == "__main__":
    app.run(port=5006, host="0.0.0.0") # this runs the app
