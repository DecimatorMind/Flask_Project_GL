from flask import Flask
from flask import render_template
from forms import SignUpForm
from forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'

@app.route("/")
def homepage():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/<int:number>")
def loop(number):
    return render_template("loop.html",number = number)

@app.route("/login",methods = ["POST","GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return render_template("login.html",message = "Successfully LoggedIn")
    return render_template("login.html",form = form)

@app.route("/signup",methods = ["POST","GET"])
def signup():
    form = SignUpForm

if __name__ == "__main__":
    app.run()