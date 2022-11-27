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

# CREATE LEMBRETE

def create_lembrete(id_mural, nome, descricao, created):
    created = date.today()

    comando = f'INSERT INTO tb_lembrete(id_mural, nome, descricao, created) VALUES ({id_mural}, {nome}, {descricao}, {created});'
    cursor.execute(comando)
    conexao.commit() 
#edita o banco de dados
#resultado = cursor.fetchall() #ler o banco de dados

# READ LEMBRETE
def read_lembrete(id_mural):
    comando = f'SELECT * FROM tb_lembrete where id_mural= {id}'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print(resultado)


#Delete 
def deleta_lembrete(id):
    comando = f'DELETE FROM tb_lembrete WHERE id = {id}'
    cursor.execute(comando)
    conexao.commit()

## Final do codigo
cursor.close()
conexao.close()