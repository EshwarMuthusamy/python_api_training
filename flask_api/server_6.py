#!/usr/bin/python3

from flask import Flask
from flask import make_response
from flask import request
from flask import render_template
from flask import url_for
from flask import redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
@app.route("/setcookie", methods = ["POST", "GET"])
def setcookie():
    if request.method == "POST":
        user = request.form["nm"]
        print(user)
        resp = make_response(render_template("readcookie.html"))

        resp.set_cookie("userID", user)

        return resp
    if request.method == "GET":
        return redirect(url_for("home"))

@app.route("/getcookie")
def getcookie():
    name = request.cookies.get("userID")

    return "<h1> welcome" + name  +  "</h1>"
        
if __name__ == "__main__":
    app.run(port=5006, host="0.0.0.0") # this runs the app
