from flask import Flask, render_template, url_for, flash, redirect
from forms import RegisterForm, LoginForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Only for Development
app.config["SECRET_KEY"] = "ed13ff47228583ac38fca4ee4f91fb19"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"

db = SQLAlchemy(app)

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