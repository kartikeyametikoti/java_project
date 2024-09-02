
import os
from flask import Flask
app = Flask(name)

@app.route("/")
def main():
return "Welcome! guru idi second_5000"

@app.route('/how are you')
def hello():
return 'I am good, how about you?'

if name == "main":
app.run(host="0.0.0.0", port=5000, debug=True)

