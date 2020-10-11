import os
from flask import Flask, request, render_template, jsonify

# from src import tf_idf as t

print(os.path.join(os.getcwd(), "src/site"))

app = Flask(__name__, template_folder=os.path.join(os.getcwd(), "src/site"))

@app.route("/")
def home():
	'''Display the homepage of notGoogle'''
	return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
	'''Process the query and find the relevant documents to display in UI.'''
	text = request.form["query"]
	# Call the search function on `text` here and save the output as a dictionary to `content`
	content = {
		'text': text
	}
	return render_template("results.html", content=content)


if __name__ == "__main__":
	app.run(debug=True)