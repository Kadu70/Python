
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

# ---------------------------------------------

cursor.execute("""
ALTER TABLE clientes
ADD COLUMN bloqueado BOOLEAN;
""")

# ALTER TABLE clientes: indica que altere a estrutura da tabela
# ADD COLUMN: comando para adicionar uma nova coluna
# bloqueado: nome da nova coluna
# BOOLEAN: tipo de dado da nova coluna
# armazenado como INTEGER
# onde 0 vale FALSE e 1 vale TRUE.

conn.commit()
print('Novo campo adicionado com sucesso')

conn.close()

