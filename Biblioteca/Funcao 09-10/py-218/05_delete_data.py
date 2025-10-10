import conexao

id_cliente = 3

conexao.cursor.execute("""
        DELETE FROM clientes
                       WHERE id = ?
""",
(id_cliente,) )

conexao.conn.commit()
print('registo excluido com sucesso!')

conexao.coon.close()