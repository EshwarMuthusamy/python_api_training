#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "JARVIS you up?"

if __name__ == "__main__":
    app.run(port=5006,host="0.0.0.0") # this runs the app
