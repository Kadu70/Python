import conexao
conexao.cursor.execute("""
      ALTER TABLE clientes ADD COLUNN bloqueado BOOLEAN;                 
                       """)
conexao.conn.commit()

print("novo campo adicionado com sucesso")

conexao.conn.close()
