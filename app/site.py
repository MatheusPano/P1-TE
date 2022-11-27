from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("login.html")


@app.route("/cadastro")
def cadastro():
    return render_template("cadastro/cadastro.html")


@app.route("/menu")
def menu():
    return render_template("menu.html")


if __name__ == "__main__":
    app.run(debug=True)
