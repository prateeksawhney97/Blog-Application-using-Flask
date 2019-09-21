from flask import Flask, escape, request, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY']='200923c1b3936dab552e984b205c527d'

posts = [
    {
    'author':'Prateek Sawhney',
    'title':'Blog post 1',
    'content':'Blog 1 content',
    'date_posted':'April 19, 2019'
    },
    {
    'author':'Sameeksha Sawhney',
    'title':'Blog post 2',
    'content':'Blog 2 content',
    'date_posted':'April 29, 2019'
    }
	

]


#setting variable app to the instance of this flask class
@app.route('/')
@app.route('/home')
#these 2 routes are handled by the same function
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET','POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__=="__main__":
    app.run(debug=True)

#running in debug mode so that we dont have to re-run the server again and again
