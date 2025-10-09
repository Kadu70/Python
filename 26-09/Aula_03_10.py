# carrinho_de_compras = [ 
# {"nome": "Teclado", "preco": 150.00}, 
# {"nome": "Mouse", "preco": 80.50}, 
# {"nome": "Monitor", "preco": 950.00}, 
# {"nome": "Cadeira Gamer", "preco": 1200.00} 
# ] 
# total_compra = 0.0 
# # Para cada 'produto' na lista 'carrinho_de_compras'... 
# for produto in carrinho_de_compras: 
# # ...pegue o preço desse produto e some ao total. 
#     preco_item = produto["preco"] 
#     total_compra += preco_item 
# print(f"Adicionando {produto['nome']} (R$ {preco_item:.2f}) ao total.") 
# print("=" * 30) 
# # A formatação :.2f garante que o valor seja exibido com duas casas decimais. 
# print(f"O valor total da compra é: R$ {total_compra:.2f}")

# lista_de_emails = ["ana@email.com", "bruno.costa@email.com", "carla123@email.com"] 
# # Para cada 'email' na 'lista_de_emails'... 
# for email in lista_de_emails: 
# # ...crie uma mensagem personalizada e simule o envio. 
#     nome_usuario = email.split('@')[0]  # Pega a parte do e-mail antes do @ 
#     mensagem = f"Olá {nome_usuario}, obrigado por se inscrever em nossa newsletter!" 
# # Aqui iria o código real para enviar o e-mail 
# print(f"Enviando para {email}: '{mensagem}'") 
# print("-" * 30) 
# print("Todos os e-mails foram enviados com sucesso!")


# import random 
 
# numero_secreto = random.randint(1, 20) 
# palpite = 0 
 
# print("Jogo de Adivinhação! Tente adivinhar o número entre 1 e 20.") 
 
# # Enquanto o 'palpite' do usuário for diferente do 'numero_secreto'... 
# while palpite != numero_secreto: 
#     # ...peça um novo palpite. 
#     try: 
#         palpite = int(input("Qual o seu palpite? ")) 
         
#         if palpite < numero_secreto: 
#             print("Muito baixo! Tente novamente.") 
#         elif palpite > numero_secreto: 
#             print("Muito alto! Tente novamente.") 
#     except ValueError: 
#         print("Por favor, digite um número válido.") 
 
# print("=" * 30) 
# print(f"Parabéns! Você acertou! O número secreto era {numero_secreto}.")

# fila_de_tarefas = ["Imprimir relatório A", "Enviar e-mail de marketing", "Fazer backup do banco de dados", "Atualizar sistema"] 
# print("Iniciando processamento da fila de tarefas...") 
# # Enquanto a 'fila_de_tarefas' não estiver vazia... 
# while len(fila_de_tarefas) > 0: 
# # ...pegue a próxima tarefa da fila (a primeira). 
#     tarefa_atual = fila_de_tarefas.pop(0)  # .pop(0) remove e retorna o primeiro item 
#     print(f"Processando: '{tarefa_atual}'...") 
#     # Simula o tempo de processamento 
#     # import time; time.sleep(1)  
#     print(f"Restam {len(fila_de_tarefas)} tarefas na fila.") 
# print("=" * 30) 
# print("Todas as tarefas foram processadas. Fila vazia!")

# usuarios_cadastrados = ["ana", "carlos", "beatriz", "daniel", "elaine"] 
# novo_usuario = "beatriz" 
# usuario_existe = False 
# print(f"Verificando se o usuário '{novo_usuario}' já existe...") 
# for usuario in usuarios_cadastrados: 
#     print(f"Comparando com '{usuario}'...") 
#     if usuario == novo_usuario: 
#         print("Usuário encontrado!") 
#         usuario_existe = True 
#         break  # Sai do laço, pois não há necessidade de continuar a busca 
#         if usuario_existe: 
#             print(f"O nome de usuário '{novo_usuario}' já está em uso.") 
#         else: 
#             print(f"O nome de usuário '{novo_usuario}' está disponível.")

# notas_alunos = [8.5, 9.0, -1.0, 7.2, 10.0, -5.0, 6.8, 11] 
# soma_notas_validas = 0.0 
# quantidade_notas_validas = 0 
# print("--- Calculando média de notas válidas ---") 
# for nota in notas_alunos: 
#     if nota < 0 or nota > 10: 
#         print(f"Nota inválida encontrada ({nota}). Ignorando...") 
#         continue  # Pula para a próxima nota, ignorando as linhas abaixo 
# # Este código só executa para notas válidas 
#     soma_notas_validas += nota 
#     quantidade_notas_validas += 1 
# media = soma_notas_validas / quantidade_notas_validas 
# print("=" * 30) 
# print(f"Média das notas válidas: {media:.2f}") 
# # O continue permite que o programa lide com dados "sujos" de forma elegante, sem interromper o processamento dos


import Biblioteca
def main():
    # i=0
    # preco=0
    # total =0
    # pagar =0
    # troco=0
    # Biblioteca.Titulo('Carrinho de Compra')
    # while(True):
    #     i+=1
    #     print(f'Produto nº {i:3}')
    #     preco= float (input('Digite o valor do produto: '))
    #     print ('\n')
    #     if preco==0:
    #         break
    #     total = total+preco
    # print (f'Valor a Pagar R$ {total:6.2f}')
        
    # while(True):
    #     pagar = float( input('Digite a quantia que ira pagar: '))
    #     if pagar >= total:
    #          break
    # troco = pagar-total
    # print (f'O valor do troco eh R$ {troco:6.2f}')
    # print ('\n')
    # Biblioteca.Titulo('FIM')
    
  
    Estoque=[]#TABELA
    total = 0 #TOTAIS DE ITENS
    preco = 0.0 #PREÇO TOTAL
    destintos = 0 #CONTA ITENS DESTINTOS
    esp = 100 # LINHA DE DEVISA

    #IMPRIMI TITULO PRE FORMATADO
    Biblioteca.Titulo('Cadastro de Produtos')

    #INICIO DE COMANDOS DE REPETIÇÃO INFINITO 
    while(True):
        #TITULO
        Biblioteca.Titulo("MENU")

        #CARREGA E RECEBE O VALOR DO MENU DE OPERAÇAO
        op = int(input( ('0 - Sair \n1 - Cadastrar \n2 - Imprimir\n ')))

        #VERIFICA  QUAL A OPCAO ESCOLHIDA

        #SE FOR ZERO
        if op==0:
            Biblioteca.Titulo( 'SAINDO')
            break #SAIR DO SISTEMA

        #SE FOR PARA INCLUSAO
        if op ==1:
            
            #IMPRIMI UMA LINHA COM A QTDE DE ESP
            print('-'*esp) 

            #TITULO
            Biblioteca.Titulo("CADASTRANDO")

            #MAIS UMA LINHA
            print('-'*esp) 

            #CRIA O DICIONARIO PARA A LINHA ATUAL
            produto = {'Cod':0,'Descricao':' ' , 'Qtde': 0, 'Preco': 0.0}

            #CARREGA OS VALORES NO DICIONARIO
            produto['Cod']= input('Digite a codigo do produto: ')
            produto['Descricao']= input('Digite a descrição do produto: ')
            produto['Qtde']= int (input('Digite a quantidade: '))
            produto['Preco']= float (input('Digite o preço: '))

            #ADICIONA A LINHA DICIONARIO NA LISTA
            Estoque.append(produto)

            #LINHA DE DIVISAO
            print('-'*esp) 

        #SE FOR 2 - AREA DE IMPRESSAO    
        if op ==2:

            #TITULO
            Biblioteca.Titulo("RELATORIO")

            #CABEÇALHO DO RELATORIO
            print('Cod  | descrição                         |    saldo   |    preço')

            #LINHA DIVISORIA
            print('-'*esp) 

            #ZERANDO OS VALORES PARA O CALCULO DE QTDE, ITENS E PREÇOS TOTAIS
            destintos = 0
            total = 0
            preco = 0.0

            #FOR (AREA DE REPETIÇÃO), QUE PERCORE AS LINHAS
            #ATRIBUINDO A VARIAVEL CHAVE O VALOR DA MESMA (DICIONARIO)
            for chave in Estoque:

                #IMPRIMI OS VALORES DA LINHA ATUAL
                print (f"{chave['Cod']:>3}  |  {chave['Descricao']:<20}             | {chave['Qtde']:>6}     |   {chave['Preco']:>6.2f}") 

                #SOMATORIA DA QTDE DE ITENS
                total = total + chave['Qtde']

                #SOMATORIO O PREÇO TOTAL DO ITEM
                preco = preco + (chave['Preco']*chave['Qtde'])

                #SOMATORIO DOS ITENS DESTINTOS
                destintos = destintos + 1

        #LINHA DIVISORIA   
        print('-'*esp)  

        #EXIBE OS VALORES TOTAIS  
        print(f'Totais {destintos:>15}                   | {total:>6}     |R$ {preco:>6.2f}')   

        #LINHA DIVISORIA
        print('-'*esp)  

        #CARREGA UM LINHA EM BRANCO 
        print("") 
           
if __name__ =="__main__":
    main()