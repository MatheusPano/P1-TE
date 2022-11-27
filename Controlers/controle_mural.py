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

# CREATE MURAL

def create_mural(nome,id_user):
    created = date.today()

    comando = f'INSERT INTO tb_mural(nome, id_user ,created) VALUES ("{nome}" ,{id_user}, "{created}");'
    cursor.execute(comando)
    conexao.commit() 
#edita o banco de dados
#resultado = cursor.fetchall() #ler o banco de dados

# READ MURAL
def read_mural(id_mural):
    comando = f'SELECT * FROM tb_mural where id = {id_mural}'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print(resultado)


#DELETE MURAL
def deleta_mural(id):
    comando = f'DELETE FROM tb_lembrete where id_mural = {id}' 
    cursor.execute(comando)
    comando = f'DELETE FROM tb_mural WHERE id = {id}'
    cursor.execute(comando)
    conexao.commit()


create_mural('Faculdade')

## Final do codigo
cursor.close()
conexao.close()