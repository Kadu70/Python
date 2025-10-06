# #########################################################################
# #18/09/2025
# x=y=z=w =False
# n1=n2=0
# n1= int(input ("digita um numero:"))
# n2= int(input ("digita um novo numero:"))

# x= n1 == n2
# print("são inguas?", x, "\n")

# z= n1 > n2
# print(n1, "é maior que", n2, "?" , z, "\n")

# y= n1!= n2
# print("são Diferente?", y, "\n")



# w= n1<5<n2

# print(n1,"e",n2, "entao entre 5", w, "\n")

#########################################################################

# n1=n2 = 0

# n1= int(input ("digita um numero:"))
# n2= int(input ("digita um novo numero:"))

# soma = n1 + n2

# print("A soma entre", n1, "e" , n2, "eh", soma)

# print(f"A soma entre {n1} com {n2} he igual a {soma}")

#########################################################################

# numero = 3.141592653589793
# print (f"pi com todas as casas decimais {numero}")

# print (f'pi com apenas 2 casas decimais {numero:.2f}')

# print (f'pi com apenas 4 casas decimais {numero:.4f}')


#########################################################################


#Varias linhas

# n1=10
# print("O numero inteiro é:",n1)
# print(f"O numero inteiro é: {n1}")


#########################################################################
# nome = "Carlos"

# print(f'seu nome é {nome}')


#########################################################################

# numero = 3.14659
# # exibir todas as casas decimais
# print(f"exibir todas as casas decimais: {numero}")

# # exibir duas as casas decimais
# print(f"exibir duas casas decimais: {numero:.2f}")

# # exibir de outra forma dusa casas decimais
# numero_arredondado = round (numero,2)
# print(f"exibir duas casas decimais: {numero_arredondado}")

# print(f'exibir duas casas decimais sem arredondamento: {int(numero *100)/100}')

# valor = 1000000
# print(f"{valor:,.2f}") # Saída: 1,000,000.00

# valor = 123
# print(f"{valor:10d}")  # Saída: "       123" (10 caracteres)
# print(f"{valor:0>10d}") # Saída: "0000000123"

# valor = 0.753
# print(f"{valor:.1%}") # Saída: 75.3%

# valor = 123.45678
# print("O valor formatado é: {:,.2f}".format(valor)) # Saída: O valor formatado é: 1,123.46


# import locale

# locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8') # Define o locale para português do Brasil
# valor = 10535.30
# print(f"R$ {valor:n}") # Saída: R$ 10.535,30


#########################################################################

# texto1 = 'ola'
# texto2=', '
# texto3= "mundo"

# print('linha5: '+ texto1+ texto2+ texto3)
# print('linha5: ', texto1, texto2, texto3)
# print(f'linha5: {texto1} {texto2} {texto3}')

#########################################################################

# nome = 'Charlie'
# idade = 35
# altura =1.75

# print ('nome: %s, Idade: %d, Altura: %s' % (nome, idade, altura))

# print (f'nome: {nome}, Idade: {idade}, Altura: {altura}')

#########################################################################

#Exemplo Divisão

# div = 3/5
# print(f'a divisão destes valores sao: {div}')
# print(f'a divisão destes valores sao: {3/5}')

# #lista
# t = (1,2,3,4,5)
# print (t[2], t[4])


# #entrada de dados
# num = int(input ('digite um valor inteiro e positivo : '))


# #estrutura de repetição para exibir o resultado
# for c in range(1,11):
#     mult = num*c
#     print ('{:2} x {:2} = {:2}'. format(num,c,mult))



#########################################################################

# Desafio01
# desenvolva um programa que some 2 numeros Inteiros
# requisitos:
#  - os 2 numeros dever ser digitados pelo usuario 
#  - utilizando a instrução print informar o usuario sobre o que o programa ira realizar
#  - executar a operação de adição utilizando o operador +
#  - mostrar para o usuario a resposta final

while True:
    n1 = int(input ('entre com um numero inteiro: '))
    n2 = int(input ('entre com outro numero inteiro: '))

    if n1==n2==0 :
        break

    soma = n1+n2
    print(f'{n1:2}  + {n2:2} = {soma:2}')

    
