# importa o modulo sqlite3
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

# ----------------------------------------------------------


cursor.execute("""
SELECT * FROM clientes;
""")

for linha in cursor.fetchall():
    print(linha)
# cursor.fetchall() 
#    -> recupera todas as linhas (registros)
#       do resultado da consulta e as retorna 
#       como uma listas de tuplas
# O loop for 
#  -> itera sobre cada linha(tupla) na 
#     lista retornada por fetchall() 
#    dentro do loop, esta linha imprime
#    cada linha (tupla) no console

conn.close














