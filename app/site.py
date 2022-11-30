from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = 'mysql',
        servidor = 'localhost',
        database = 'bd_python'
    )

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True )
    usuario = db.Column(db.String(45), nullable=False)
    senha = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(15), nullable=False)
    sexo = db.Column(db.String(1), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    created = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name


class Murais(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True )
    nome = db.Column(db.String(45), nullable=False)
    created = db.Column(db.Date, nullable=False)
    tblembretes = db.relationship('Lembretes', backref='murais', lazy=True) 

    def __repr__(self):
        return '<Name %r>' % self.name

class Lembretes(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True )
    id_mural = db.Column(db.Integer, db.ForeignKey('mural.id'), nullable=False)
    nome = db.Column(db.String(45), nullable=False)
    descricao = db.Column(db.String(200), nullable=False)
    created = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name


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