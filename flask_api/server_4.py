#!/usr/bin/python3

from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/success/<name>",methods=['POST'])
def success(name):
    if request.method == 'POST':
        return 'Welcome{}\n'.format(name)
@app.route("/")
def index():
    return render_template("login.html")
@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == 'POST':
        nm = request.form.get("nm")
        return redirect(url_for("success",name=nm), code=302)     
    else:
        return redirect(url_for("index"))
    

if __name__ == "__main__":
    app.run(port=5006,host="0.0.0.0") # this runs the app
