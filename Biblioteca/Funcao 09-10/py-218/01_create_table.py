
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

# cria uma tabela
cursor.execute("""
            create table  clientes (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER,
            cpf VARCHAR(11) NOT NULL,
            email TEST NOT NULL,
            fone TEXT,
            cidade TEXT,
            uf VARCHAR(2) NOT NULL,
            data_registro DATE NOT NULL
            );
""")

print ('tabela criada com sucesso')

# desconectado
conn.close()