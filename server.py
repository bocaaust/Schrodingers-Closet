from flask import Flask
from flask import render_template

app = Flask(__name__)

import db_model as db
import json

from datetime import date
from datetime import timedelta

@app.route("/offer")
def index():

    results = db.post_item()

    return render_template("offer.html")

@app.route("/signup")
def signup():

	results = db.create_account()

	return render_template("signup.html")

@app.route("/")
@app.route("/setup")
def setup():
    results = db.setup()
    
    return render_template("index.html")



if __name__ == "__main__":
    app.run('0.0.0.0')
