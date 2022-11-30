from datetime import date
import mysql.connector
from mysql.connector import errorcode

print("Conectando...")
try:
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='mysql'
    )
except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Existe algo errado no nome de usuário ou senha')
      else:
            print(err)

cursor = conexao.cursor()

cursor.execute("DROP DATABASE IF EXISTS `bd_python`;")

cursor.execute("CREATE DATABASE `bd_python`;")

cursor.execute("USE `bd_python`;")

#criando tabelas

TABELAS = {}
TABELAS['User'] = ('''
    CREATE TABLE `tb_users` (
    `id` int NOT NULL AUTO_INCREMENT,
    `usuario` varchar(45) DEFAULT NULL,
    `senha` varchar(45) DEFAULT NULL,
    `email` varchar(100) DEFAULT NULL,
    `telefone` varchar(15) DEFAULT NULL,
    `sexo` varchar(1) DEFAULT NULL,
    `data_nascimento` date DEFAULT NULL,
    `created` date DEFAULT NULL,
    PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
''')

TABELAS['Murais'] = ('''
    CREATE TABLE `tb_mural` (
    `id` int NOT NULL AUTO_INCREMENT,
    `nome` varchar(45) DEFAULT NULL,
    `created` date DEFAULT NULL,
    PRIMARY KEY (`id`)
    ) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
''')

TABELAS['Lembretes'] = ('''
    CREATE TABLE `tb_lembrete` (
    `id` int NOT NULL AUTO_INCREMENT,
    `id_mural` int NOT NULL,
    `nome` varchar(45) DEFAULT NULL,
    `descricao` varchar(200) DEFAULT NULL,
    `created` date DEFAULT NULL,
    PRIMARY KEY (`id`),
    KEY `fk_id_mural_idx` (`id_mural`),
    CONSTRAINT `fk_id_mural` FOREIGN KEY (`id_mural`) REFERENCES `tb_mural` (`id`)
    ) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

''')


for tabela_nome in TABELAS:
    tabela_sql = TABELAS[tabela_nome]
    try:
            print('Criando tabela {}:'.format(tabela_nome), end=' ')
            cursor.execute(tabela_sql)
    except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print('Já existe')
            else:
                print(err.msg)
    else:
        print('OK')

#CRUD

# CREATE USER

def create_user(usuario='', senha='', email='', telefone='', sexo='', data_nascimento=''):
    created = date.today()

    comando = f'INSERT INTO tb_users (usuario, senha, email, telefone, sexo, data_nascimento, created) VALUES ("{usuario}", "{senha}", "{email}", "{telefone}", "{sexo}", "{data_nascimento}", "{created}");'
    cursor.execute(comando)
    conexao.commit() 

# READ USER
def read_user(id):
    comando = f'SELECT * FROM tb_users where id= {id}'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print(resultado)


#CRUD

# CREATE LEMBRETE

def create_lembrete(id_mural, nome, descricao):
    created = date.today()

    comando = f'INSERT INTO tb_lembrete(id_mural, nome, descricao, created) VALUES ({id_mural}, "{nome}", "{descricao}", "{created}");'
    cursor.execute(comando)
    conexao.commit() 

# READ LEMBRETE
def read_lembrete(id_mural):
    comando = f'SELECT * FROM tb_lembrete where id_mural= {id_mural}'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print(resultado)


#Delete 
def deleta_lembrete(id):
    comando = f'DELETE FROM tb_lembrete WHERE id = {id}'
    cursor.execute(comando)
    conexao.commit()


# CREATE MURAL

def create_mural(nome, id_user):
    created = date.today()

    comando = f'INSERT INTO tb_mural(nome, created) VALUES ("{nome}", {id_user}, "{created}");'
    cursor.execute(comando)
    conexao.commit() 


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


## Final do codigo
cursor.close()
conexao.close()