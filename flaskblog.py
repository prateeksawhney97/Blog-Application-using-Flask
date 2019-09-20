from flask import Flask, escape, request

app = Flask(__name__)
#setting variable app to the instance of this flask class
@app.route('/')
def hello():
    return "<h1>Home Page</h1>"

@app.route('/about')
def about():
    return "<h1>About Page</h1>"

if __name__=="__main__":
    app.run(debug=True)

#running in debug mode so that we dont have to re-run the server again and again
