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


id_cliente = 1
novo_fone = "11-9500-2011"
novo_nome = "Paulo Souza"
novo_data_registro = '2025-06-11'

cursor.execute("""
UPDATE clientes
SET fone = ?, nome = ?, data_registro = ?
WHERE id = ?
""", (novo_fone, novo_nome, novo_data_registro, id_cliente))

conn.commit()

print("Dados atualizados com sucesso!!")

conn.close()

