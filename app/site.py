from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def login():
    return render_template('login/login.html')

@app.route("/cadastro")
def cadastro():
    return render_template('cadastro/cadastro.html')

@app.route("/menu")
def menu():
    return render_template('menu/menu.html')

@app.route("/murais")
def murais():
    return render_template('murais/murais.html')

@app.route("/lembretes")
def lembretes():
    return render_template('lembretes/lembretes.html')

@app.route("/user")
def users():
    return render_template('user/user.html')

if __name__ == "__main__":
    app.run(debug=True)