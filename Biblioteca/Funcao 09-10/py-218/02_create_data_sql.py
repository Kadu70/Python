import sqlite3
import os
db_folder = '/workspaces/Python/Biblioteca/Funcao 09-10/py-218'
db_file = 'clientes.db'
db_path = os.path.join(db_folder,db_file)

os.makedirs(db_folder, exist_ok=True)

# conectando db
conn = sqlite3.connect(db_path)

# defini o cursor
cursor = conn.cursor()

cursor.execute("""
            INSERT INTO clientes (
                nome ,
                idade,
                cpf ,
                email,
                fone ,
                cidade,
                uf ,
                data_registro )
            VALUES(
               'Rodrigo',
               30,
               '169.855.398-13',
               'rs30@email.com',
               '11-5500-6363',
               'Sao Paulo',
               'SP',
               '2025-06-08'
               )   
            
""")

cursor.execute("""
            INSERT INTO clientes (
                nome ,
                idade,
                cpf ,
                email,
                fone ,
                cidade ,
                uf ,
                data_registro )
            VALUES(
               'Mouro',
               25,
               '119.125.398-13',
               'mauro@email.com',
               '11-2250-6300',
               'Maua',
               'SP',
               '2000-09-08'
               )   
            
""")

# cravando no hs
conn.commit()

print('dados inseridos com sucessos')

conn.close()