import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello Home page"

@app.route('/greeting')
def hello_greeting():
    name = os.getenv("GREETING_MSG_NAME", "World")
    return f"hello {name}!"
