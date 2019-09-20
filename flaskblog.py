from flask import Flask, escape, request

app = Flask(__name__)
#setting variable app to the instance of this flask class
@app.route('/')
def hello():
    return "Hello World!"
