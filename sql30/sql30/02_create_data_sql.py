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




cursor = conn.cursor()

# inserindo dados na tabela
cursor.execute("""
INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, data_registro)
VALUES ('Rodrigo', 30, '169.855.398-13', 'rd30@email.com', '11-5500-6363', 'São Paulo', 'SP', '2025-06-08')
""")

cursor.execute("""
INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, data_registro)
VALUES ('Mauro', 25, '119.125.398-13', 'mauro@email.com', '11-2250-6300', 'Mauá', 'SP', '2000-09-08')
""")

# gravando no hd
conn.commit()

print('Dados inseridos com sucesso.')

conn.close()


