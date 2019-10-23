#!/usr/bin/python3

from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/<username>")
def index(username):
    return render_template("hello_basic.html",username=username)
    

if __name__ == "__main__":
    app.run(port=5006,host="0.0.0.0") # this runs the app
