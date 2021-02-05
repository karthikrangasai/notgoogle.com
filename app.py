import os
import re
from flask import Flask, request, render_template, jsonify
from src import search

reg_exp = "(n|l|a|b)"

app = Flask(__name__, template_folder=os.path.join(os.getcwd(), "src/site"))

@app.route("/")
def home():
	"""
	Display the homepage of notGoogle
	"""
	return render_template("index.html")

@app.route("/search", methods=["POST"])
def search_request():
	"""
	Process the query and find the relevant documents to display in UI.
	"""
	text = request.form["query"]
	smart = request.form["smart"]
	if re.match(reg_exp, smart) is None:
		return render_template("index.html")
	
	movies = search.search(text, smart)
	content = {
		'text': text,
		'movies' : movies
	}
	return render_template("results.html", content=content)

if __name__ == "__main__":
	app.run(debug=True)