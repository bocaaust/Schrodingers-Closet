from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

import db_model as db
import json

from datetime import date
from datetime import timedelta

@app.route("/post_offer", methods=['GET', 'POST'])
def post_offer():
	if request.method == 'POST':
		results = db.create_request(request.form['item_id'],request.form['username'],request.form['w_day'],request.form['start_time'],request.form['end_time'])
	return render_template("offer.html")

@app.route("/post_item", methods=['GET', 'POST'])
def postitem():
	if request.method == 'POST':
		results = db.post_item(request.form['item_name'],request.form['price'],request.form['state'],request.form['username'],request.form['photo'])
	return render_template("offer.html")
@app.route('/signup', methods=['GET', 'POST'])
def signup():
	if request.method == "POST":
		print request.form['username']

		results = db.create_account(request.form['username'],request.form['password'],request.form['geography'])
		return render_template("index.html")
	else:
		return render_template("signup.html")

@app.route('/search_item', methods=['GET', 'POST'])
def searchItem():
	if request.method == 'POST':
		results = db.search_item(request.form['item_form'])
	return render_template("search.html")

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

@app.route("/search.html")
def search():
	return render_template("search.html")



if __name__ == "__main__":
	app.run('0.0.0.0')
