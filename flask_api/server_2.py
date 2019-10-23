#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Wake up jarvis"

@app.route("/hello/<name>")
def hello(name):
    return "Hey {}. I am up".format(name)


if __name__ == "__main__":
    app.run(port=9878)
