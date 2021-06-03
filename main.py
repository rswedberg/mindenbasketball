import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
  return render_template("index.html")

if __name__ == '__main__':
  # Run the Flask app
  app.run(
	host='0.0.0.0',
	debug=True,
	port=8080
  )