import sqlite3
import os

# Obtenha o diretório do script atual
# __file__ é o caminho do arquivo do script em execução
script_dir = os.path.dirname(os.path.abspath(__file__))

#  Construa o caminho absoluto para o banco de dados
#  Se o script 'select.py' estiver em '.../19_08.10/sql30/' 
#  e o 'clientes.db' estiver DENTRO de 'sql30',
#  então o 'clientes.db' está na mesma pasta do script.
#  Se for esse o caso, o caminho correto é:
db_path = os.path.join(script_dir, 'clientes.db')

# Se 'clientes.db' estivesse na pasta 'sql30' E SEU SCRIPT ESTIVESSE NO DIRETÓRIO PAI
# por exemplo: script em '.../19_08.10/meu_script.py' e db em '.../19_08.10/sql30/clientes.db'
# Aí sim você usaria: db_path = os.path.join(script_dir, 'sql30', 'clientes.db')


conn = None # Inicializa conn como None para ser acessível fora do try
try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    print("Conexão bem-sucedida ao banco de dados!")
    print(f"Banco de dados conectado: {db_path}")

    # Mova a lógica de consulta para DENTRO do bloco try
    while True:
        #  Solicitar o ID ao usuário
        id_str = input("\nDigite o ID do cliente que deseja consultar (ou 'sair' para finalizar): ")

        if id_str.lower() == 'sair':
            print("Consulta finalizada.")
            break

        try:
            cliente_id = int(id_str)
        except ValueError:
            print("ID inválido. Por favor, digite um número inteiro.")
            continue

        #  Executa a consulta SELECT com a cláusula WHERE para buscar pelo ID
        #  Entende que a tabela tem colunas id, nome, idade, cpf, email, fone, cidade, uf, data_registro
        cursor.execute("SELECT id, nome, idade, cpf, email, fone, cidade, uf, data_registro FROM clientes WHERE id = ?", (cliente_id,))

        #  Recuperar o resultado
        cliente = cursor.fetchone() 
        #  fetchone() retorna uma tupla para uma única linha ou None

        #  Exibir o resultado
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

except sqlite3.OperationalError as e:
    print(f"Erro ao abrir o banco de dados: {e}")
    print(f"Caminho tentado: {db_path}")
    print("Verifique se o arquivo do banco de dados existe e o caminho está correto.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
finally:
    # Este bloco é executado sempre, garantindo que a conexão seja fechada
    if conn:
        conn.close()
        print("\nConexão com o banco de dados fechada.")
