from flask import Flask
app = Flask(__name__)

@app.route("/python")
def hello_world():
    return "<p>Hello, World!</p><br/><p>This is a Python Flask API</p>"