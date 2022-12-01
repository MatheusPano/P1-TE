from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.secret_key = 'bdpython'

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

    def __repr__(self):
        return '<Name %r>' % self.name


class Murais(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True )
    nome = db.Column(db.String(45), nullable=False) 

    def __repr__(self):
        return '<Name %r>' % self.name

class Lembretes(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True )
    nome = db.Column(db.String(45), nullable=False)
    descricao = db.Column(db.String(200), nullable=False)

    #Cria e retorna uma string para nois, quando a classe é acessada em modo interativo.
    def __repr__(self):
        return '<Name %r>' % self.name


@app.route("/login")
def login():
    return render_template('login/login.html')


@app.route('/autenticar', methods=['POST',])
def autenticar():
    usuaario = User.query.filter_by(usuario=request.form['nome']).first()
    if usuaario:
        if request.form['senha'] == usuaario.senha:
            session['usuario_logado'] = usuaario.usuario
            flash(usuaario.usuario + ' logado com sucesso!')
            return redirect(url_for('menu'))
    else:
        flash('Usuario ou senha incorreto.')
        return redirect(url_for('login'))



@app.route('/cadastro')
def cadastro():
    return render_template('cadastro/cadastro.html')


@app.route("/criarUsuario", methods=['POST',])
def criarUsuario():

    nome=request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    
    usuaario = User.query.filter_by(usuario=nome).first()

    if usuaario:
        flash('Usuário Já Existente!')
        return redirect(url_for('login'))

    novo_usuario = User(usuario=nome, senha=senha, email=email)
    db.session.add(novo_usuario)
    db.session.commit()

    return redirect(url_for('login'))

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
    usuarioAtual = session['usuario_logado']
    flash('Olá ',usuarioAtual)
    return render_template('user/user.html')

if __name__ == "__main__":
    app.run(debug=True)



