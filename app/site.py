from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("sobre.html")

@app.route("/cadastro")
def cadastro():
    return "oi"

@app.route("/menu")
def menu():
    return "menu"




if __name__ == "__main__":
    app.run(debug=True)