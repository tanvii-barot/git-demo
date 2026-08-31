from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello Home Screen"

@app.route('/greeting')
def hello_greeting():
    return "hello World!"
