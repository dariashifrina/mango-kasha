from flask import Flask, session, url_for, redirect, render_template, request

import os
import urllib2
import json

#App instantiation
app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == "__main__":
    app.debug = True
    app.run()
