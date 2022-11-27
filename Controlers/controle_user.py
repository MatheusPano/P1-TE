from datetime import date
import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='mysql',
    database='bd_python',
)

cursor = conexao.cursor()

#CRUD

# CREATE USER

def create_user(usuario='', senha='', email='', telefone='', sexo='', data_nascimento=''):
    created = date.today()

    comando = f'INSERT INTO tb_users (usuario, senha, email, telefone, sexo, data_nascimento, created) VALUES ("{usuario}", "{senha}", "{email}", "{telefone}", "{sexo}", "{data_nascimento}", "{created}");'
    cursor.execute(comando)
    conexao.commit() 
#edita o banco de dados
#resultado = cursor.fetchall() #ler o banco de dados

# READ USER
def read_user(id):
    comando = f'SELECT * FROM tb_users where id= {id}'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print(resultado)


## Final do codigo
cursor.close()
conexao.close()