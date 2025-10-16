# criando tabela
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


# ------------------------------------------

# definir cursor
cursor = conn.cursor()

# criação da tabela
cursor.execute("""
CREATE TABLE clientes (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome    TEXT NOT NULL,
        idade   INTEGER,
        cpf     VARCHAR(11) NOT NULL,
        email   TEXT NOT NULL,
        fone    TEXT,
        cidade  TEXT,
        uf      VARCHAR(2) NOT NULL,
        data_registro   DATE NOT NULL    
);    
""")

print('Tabela criada com sucesso.')
# desconectando
conn.close()
