
import sqlite3
import os

# Definindo o caminho para o banco de dados
db_folder = 'E:/01 Entidades de Ensino/01 HD_Senai/01 TURMAS/05 2025/08_BTA-PRPY-218_TARDE/mes_10/14_10.10/sql30'
db_file = 'clientes.db'
db_path = os.path.join(db_folder, db_file)

# Verifica se o diretório existe, caso contrário, cria-o
os.makedirs(db_folder, exist_ok=True)

# conectando bd ..
conn = sqlite3.connect(db_path) # Usando o caminho construído

cursor = conn.cursor()
# variavel cursor armazena  o  objeto cursor

# -----------------------------------------------------

# define uma variavel id_cliente com o valor 3
id_cliente = 2

# excluir um registro da tabela
cursor.execute("""
DELETE FROM clientes
WHERE id = ?
""",(id_cliente,))
# a linha instrui o banco de dados a remover
# o registro da tabela clientes onde a coluna id tem valor 3

conn.commit()

print('Registro excluido com sucesso !')

conn.close()