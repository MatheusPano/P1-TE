from flask import Flask, render_template, request, redirect, url_for
from Controlers import controle_user as cu

app = Flask(__name__)

@app.route("/")
def login():
    return render_template('login/login.html')

@app.route("/cadastro", methods=['POST',])
def cadastro():
    nome=request.form.get("nome")
    email = request.form.get("email")
    tel = request.form.get("telefone")
    genero = request.form.get("genero")
    dt_nasc = request.form.get("data")
    senha = request.form.get("senha")
    
    cu.create_user(nome, senha ,email, tel, genero, dt_nasc)

    return redirect('menu/menu.html')

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