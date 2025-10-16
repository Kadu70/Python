# 03_create_data_param.py --> PARAMETROS
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

# --------------------------------------


# solicitando os dados ao usuário
p_nome = input('Digite Nome: ')
p_idade = input('Digite a Idade: ')
p_cpf = input('Digite CPF - (11 digitos): ')
p_email = input('Digite Email: ')
p_fone = input('Digite Fone: ')
p_cidade = input('Digite a Cidade: ')
p_uf = input('Digite UF: ')
p_data_registro = input('Registrado em (aaaa-mm-dd): ')

# inserindo dados na tabela
cursor.execute("""
INSERT INTO clienteS (nome, idade, cpf, email, fone, cidade, uf, data_registro)
VALUES (?,?,?,?,?,?,?,?)
""", (p_nome, p_idade, p_cpf, p_email, p_fone, p_cidade, p_uf, p_data_registro))

conn.commit()

print('Dados inseridos com sucesso.')

conn.close()