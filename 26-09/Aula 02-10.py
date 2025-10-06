# # Uma lista onde cada item é uma string (texto) 
# tarefas_do_dia = ['Lavar a louça', 'Estudar Python', 'Ir à academia', 'Fazer compras'] 
# # Adicionar uma nova tarefa 
# tarefas_do_dia.append('Ler um livro') 
# print("Minhas tarefas para hoje:") 
# for tarefa in tarefas_do_dia: 
#     print(f"- {tarefa}") 
    
# import platform  
#     # Cada lista interna representa as notas de um aluno 
# tabela_de_notas = [ 
#     ['Ana', 8.5, 9.0],    # Aluno 1: Nome, Nota Prova 1, Nota Prova 2 
#     ['Bruno', 7.0, 6.5],   # Aluno 2 
#     ['Carla', 9.5, 10.0]   # Aluno 3 
# ] 
# # Acessar a nota da segunda prova de Bruno (linha 1, coluna 2) 
# nota_bruno = tabela_de_notas[1][2] 
# nota_carla = tabela_de_notas[2][2] 


# print(f"A segunda  nota de {tabela_de_notas[1][0]:7} foi: {nota_bruno:5.2f}") # Saída: A segunda nota de Bruno foi: 6.5 
# print(f"A segunda  nota da {tabela_de_notas[2][0]:7} foi: {nota_carla:5.2f}") 
# print(f"A primeira nota da {tabela_de_notas[0][0]:7} foi: {tabela_de_notas[0][1]:5.2f}") 

# # Imprimir o nome de todos os alunos 
# print("\nAlunos na turma:") 
# print("\n Nome            Nota1    Nota2   Media") 
# for aluno in tabela_de_notas: 
#     media = aluno[1] + aluno[2]
#     print(f"- {aluno[0]:12} - {aluno[1]:5.2f}  - {aluno[2]:5.2f} - {media/2:5.2f}")
    
    
# numeros_pares = [] # Começamos com uma lista vazia 
# numeros_impares = [] 
# print("Digite 5 números e eu guardarei os pares.") 
# for i in range(5): 
#     numero = int(input(f"Digite o {i+1}º número: ")) 
#     if numero % 2 == 0:  # Verifica se o número é par 
#         if numero !=0:
#            numeros_pares.append(numero) 
#     else:
#         numeros_impares.append(numero) 

# if len(numeros_pares)>0: 
#     print(f"\nOs números pares que você digitou foram:   {numeros_pares}")
# else:
#     print(f"\nNão encontrado numeros pares")
# if len(numeros_impares)>0:
#     print(f"\nNão encontrado numeros impares")
# else:
#     print(f"\nOs números impares que você digitou foram: {numeros_impares}")
        
    
# dic_dados = {'nome': 'Alice','idade':35, 'cidade': 'São Paulo'}    
# # exibindo a lista
# print("\nlista original")
# print (dic_dados)

# # adicionar novo para chave-valor
# dic_dados['profissao']= 'dentista'

# # exibindo o dicionario alterado
# print("\nlista atualizada com o campo profissao")
# print (dic_dados)

# # alterando o valor da idade
# print("\nlista com a idade alterada")
# dic_dados['idade']=40
# print (dic_dados)

# # exibe o valor de cidade
# print("\nCidade: ")
# print(dic_dados['cidade'])

import Biblioteca


def main():
    
    candidato = [0,0,0,0]
    cpf =0
    Biblioteca.Titulo('Votação')
    while(True):
        cpf= int(input("Digite o seu cpf: "))
        if cpf == 0:
            break
        voto = int (input ("qual o seu canditado (1 ou 2 ou 3): "))
        if (voto > 0 and  voto < 4):
            candidato[voto-1] = candidato[voto-1]+ 1
            
        else:
            candidato[3]=candidato[3]+1


    Biblioteca.Titulo(f'Candidato 01 teve {candidato[0]} votos')
    Biblioteca.Titulo(f'Candidato 02 teve {candidato[1]} votos')
    Biblioteca.Titulo(f'Candidato 03 teve {candidato[2]} votos')
    Biblioteca.Titulo(f'Nulos teve  {candidato[3]} votos')

if __name__ =="__main__":
    main()