from flask import Flask, escape, request, render_template

app = Flask(__name__)
#setting variable app to the instance of this flask class
@app.route('/')
@app.route('/home')
#these 2 routes are handled by the same function
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__=="__main__":
    app.run(debug=True)

#running in debug mode so that we dont have to re-run the server again and again
