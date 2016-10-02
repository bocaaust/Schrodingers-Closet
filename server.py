from flask import Flask
from flask import render_template

app = Flask(__name__)

import db_model as db
import json

from datetime import date
from datetime import timedelta

@app.route("/offer")
def offer():

    results = db.post_item()

    return render_template("offer.html")

@app.route("/signup")
def signup():

	results = db.create_account()

	return render_template("signup.html")

@app.route("/formcalling", methods=[GET, POST]):
def formcalling():

	print requests.get_data()

	results = db.create_account(requests.get_data[username])
	print results
	render render_template("page.html", items=results)

@app.route("/")
def index():    
    return render_template("index.html")



if __name__ == "__main__":
    app.run('0.0.0.0')
