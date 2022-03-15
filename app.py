from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/<int:number>")
def loop(number):
    return render_template("loop.html",number = number)

@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run()