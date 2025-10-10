import conexao

p_nome = input('Digite nome: \n')
p_idade = input('Digite idade: \n')
p_cpf = input('Digite cpf: \n')
p_email = input('Digite email: \n')
p_fone = input('Digite fone: \n')
p_cidade = input('Digite cidade: \n')
p_uf = input('Digite uf: \n')
p_data_registro = input('Digite data de registro: \n')


# inserindo dados na tabela

conexao.cursor.execute("""
            INSERT INTO clientes (
                nome ,
                idade,
                cpf ,
                email,
                fone ,
                cidade,
                uf ,
                data_registro )
            VALUES(?,?,?,?,?,?,?,?)""",(
                p_nome ,
                p_idade ,
                p_cpf ,
                p_email,
                p_fone,
                p_cidade,
                p_uf,
                p_data_registro 
                )
            
            )
conexao.conn.commit()

print('dados inseridos com sucesso')

conexao.conn.close ()


