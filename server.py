from flask import Flask, request, render_template, redirect
from backend import wordpost
import json

app = Flask(__name__)
wp = wordpost()
#//
#API
#//
@app.route("/get-words", methods = ["GET"])
def get_words():
	response = {
		"words": wp.get_words()
	}
	return response

@app.route("/add-word", methods = ["POST"])
def add_word():
	data = request.get_json()
	wp.add_word(data["word"])
	return "Added Sucessfully"

@app.route("/del-word", methods = ["POST"])
def del_word():
	data = request.get_json()
	wp.del_word(data["word"])
	return "Deleted Sucessfully"
#//
#Web App
#//
@app.route("/", methods = ["GET"])
def index():
	return render_template("index.html", wordlist = wp.get_words())

@app.route("/add-submit", methods = ["POST"])
def add_submit():
	word = request.form.get("word-input")
	wp.add_word(word)
	return redirect("/")

#if(__name__ == "__main__"):
#	app.run(host = "0.0.0.0", port = 80)