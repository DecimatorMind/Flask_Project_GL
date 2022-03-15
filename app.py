from site import USER_SITE
from flask import Flask
from flask import render_template
from forms import SignUpForm
from forms import LoginForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users_GL.db'
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    full_name = db.Column(db.String)
    email = db.Column(db.String,unique = True)
    password = db.Column = db.Column(db.String)

db.create_all()

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
    form = SignUpForm()
    if form.validate_on_submit():
        new = Users(full_name = form.full_name.data,email = form.email.data,password = form.password.data)
        db.session.add(new)
        try:
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
            return render_template("signup.html",message = "Failed to Signup the User")
        finally:
            db.session.close()
        return render_template("signup.html",message = "User Signup Successfull")
    return render_template("signup.html",form = form)

@app.route("/userinfo")
def userinfo():
    userlist = Users.query.all()
    return render_template("userinfo.html",userlist = userlist)

if __name__ == "__main__":
    app.run()