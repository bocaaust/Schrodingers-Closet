from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

import db_model as db
import json

from datetime import date
from datetime import timedelta

@app.route("/post_item")
def offer():

    results = db.post_item()

    return render_template("offer.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	if request.method == "POST":
		print request.form['username']

		results = db.create_account(request.form['username'],request.form['password'],request.form['geography'])
		return render_template("index.html")
	else:
		return render_template("signup.html")

"""
@app.route("/formcalling", methods=[GET, POST]):
def formcalling():

	print requests.get_data()

	results = db.create_account(requests.get_data[username])
	print results
	render render_template("page.html", items=results)
"""
@app.route("/")
def index():    
    return render_template("index.html")

@app.route("/signup.html")
def sign_up():
	return render_template("signup.html")

@app.route("/offer.html")
def offer():
	return render_template("offer.html")



if __name__ == "__main__":
    app.run('0.0.0.0')
