import conexao
conexao.cursor.execute("""
                SELECT * FROM clientes
                """)
for linha in conexao.cursor.fetchall():
    print (linha)
    # print(linha[1])

conexao.conn.close()

# fetchall => recuera todas as linhas (registros)
# do resultado da consulta e as retorna
# como uma lista de tuplas    

# o loop for -> itera sobre cada linha (tubla)na
# lista retornada por fetchall
# dentro do loop, esta linha imprime
# cada linha (tupla) no console