from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegisterForm, LoginForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Only for Development
app.config["SECRET_KEY"] = "ed13ff47228583ac38fca4ee4f91fb19"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"

db = SQLAlchemy(app)

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(15), unique=True, nullable=False)
  email = db.Column(db.String(100), unique=True, nullable=False)
  password = db.Column(db.String(60), nullable=False)
  profile_picture = db.Column(db.String(20), nullable=False, default="avatar.jpeg")
  posts = db.relationship("Post", backref="author", lazy=True)

class Post(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100), nullable=False, unique=True)
  body = db.Column(db.Text, nullable=False)
  date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

@app.route("/")
@app.route("/home")
def home():
  return render_template("index.html")

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/login")
def login():
  form = LoginForm()
  return render_template("login.html", form=form)

@app.route("/register", methods=["GET", "POST"])
def register():
  form = RegisterForm()
  if form.validate_on_submit():
    flash(f"Account created for {form.email.data}", "success")
    return redirect("login")
  return render_template("register.html", form=form)

# Only for Development
if __name__ == "__main__":
  app.run(debug=True)