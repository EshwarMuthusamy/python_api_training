#!/usr/bin/python3

from flask import Flask
from flask import redirect
from flask import url_for

app = Flask(__name__)

@app.route("/admin")
def hello_admin():
    return "Hey Boss! "
@app.route("/guest/<intruder>")
def guest(intruder):
    if intruder == "admin":
        return redirect(url_for("signin",name=intruder))
    else:
        return "Hey {}. I am jarvis".format(intruder)
@app.route("/signin/<name>")
def signin(name):
    if name  == "admin":
        return redirect(url_for("hello_admin"))
    else:
        return redirect(url_for("guest",intruder = name))

if __name__ == "__main__":
    app.run(port=5006,host="0.0.0.0") # this runs the app
