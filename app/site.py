from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.secret_key = 'bdpython'

app.config['SQLALCHEMY_DATABASE_URI'] = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD='mysql+mysqlconnector',
        usuario='root',
        senha='mysql',
        servidor='localhost',
        database='bd_python'
)

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usuario = db.Column(db.String(45), nullable=False)
    senha = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name


class Mural(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(45), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name


class Lembrete(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(45), nullable=False)
    descricao = db.Column(db.String(200), nullable=False)

    # Cria e retorna uma string para nois, quando a classe é acessada em modo interativo.
    def __repr__(self):
        return '<Name %r>' % self.name


@app.route("/")
def inicio():
    return redirect(url_for('login'))


@app.route("/login")
def login():
    return render_template('login/login.html')


@app.route('/autenticar', methods=['POST', ])
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


@app.route("/criarUsuario", methods=['POST', ])
def criarUsuario():

    nome = request.form['nome']
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


@app.route("/logout")
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('login'))


@app.route("/menu")
def menu():
    return render_template('menu/menu.html')


@app.route("/sobre")
def sobre():
    return render_template('sobre/sobre.html')


@app.route("/murais")
def murais():
    listamurais = Mural.query.order_by(Mural.id)
    return render_template('murais/murais.html', murais=listamurais)


@app.route("/criarMural", methods=['POST', ])
def criarMural():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))

    mural = request.form['mural']

    novo_mural = Mural(nome=mural)
    db.session.add(novo_mural)
    db.session.commit()

    return redirect(url_for('murais'))


@app.route("/deletarMural/<int:idMural>")
def deletarMural(idMural):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))

    mural = Mural.query.filter_by(id=idMural).delete()
    db.session.commit()
    flash("Mural Deletado com Sucesso")
    return redirect(url_for('murais'))


@app.route("/lembretes")
def lembretes():
    listalembrete = Lembrete.query.order_by(Lembrete.id)
    return render_template('lembretes/lembretes.html', lembretes=listalembrete)


@app.route("/criarLembrete", methods=['POST', ])
def criarLembrete():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))

    nome = request.form['lembrete-title']
    descricao = request.form['lembrete-text']

    novo_lembrete = Lembrete(nome=nome, descricao=descricao)
    db.session.add(novo_lembrete)
    db.session.commit()

    return redirect(url_for('lembretes'))


@app.route("/deletarLembrete/<int:idLembrete>")
def deletarLembrete(idLembrete):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))

    lembrete = Lembrete.query.filter_by(id=idLembrete).delete()
    db.session.commit()
    flash("Lembrete Deletado com Sucesso")
    return redirect(url_for('lembretes'))


@app.route("/user")
def users():
    usuarioAtual = session['usuario_logado']
    flash('Olá ',usuarioAtual)
    return render_template('user/user.html')


if __name__ == "__main__":
    app.run(debug=True)



