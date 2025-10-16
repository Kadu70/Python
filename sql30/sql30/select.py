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

# ---------------------------------------------------

while True:
            # 2. Solicitar o ID ao usuário
            id_str = input("\nDigite o ID do cliente que deseja consultar (ou 'sair' para finalizar): ")
            
            if id_str.lower() == 'sair':
                print("Consulta finalizada.")
                break
            
            try:
                cliente_id = int(id_str)
            except ValueError:
                print("ID inválido. Por favor, digite um número inteiro.")
                continue

            # 3. Executar a consulta SELECT com a cláusula WHERE para buscar pelo ID
            # Assumimos que a tabela tem colunas id, nome, email, telefone
            cursor.execute("SELECT id, nome, idade, cpf, email, fone, cidade, uf, data_registro FROM clientes WHERE id = ?", (cliente_id,))
            
            # 4. Recuperar o resultado
            cliente = cursor.fetchone() # fetchone() retorna uma tupla para uma única linha ou None

            # 5. Exibir o resultado
            if cliente:
                print("\n--- Cliente Encontrado ---")
                print(f"ID: {cliente[0]}")
                print(f"Nome: {cliente[1]}")
                print(f"Idade: {cliente[2]}")
                print(f"Cpf: {cliente[3]}")
                print(f"Email: {cliente[4]}")
                print(f"Fone: {cliente[5]}")
                print(f"Cidade: {cliente[6]}")
                print(f"UF: {cliente[7]}")
                print(f"Data Registro: {cliente[8]}")
                print("--------------------------")
            else:
                print(f"Nenhum cliente encontrado com o ID {cliente_id}.")

