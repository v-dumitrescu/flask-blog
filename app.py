from flask import Flask, render_template, url_for
from forms import RegisterForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "ed13ff47228583ac38fca4ee4f91fb19"

@app.route("/")
@app.route("/home")
def home():
  return render_template("index.html")

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/register")
def register():
  form = RegisterForm()
  return render_template("register.html", form=form)

if __name__ == "__main__":
  app.run(debug=True)