# 19/09
# DEFINIÇÃO DOS ELEMENTOS COMUNS EM SCRIPTS Python

# def main():
#     if _name_ == '_main _':
#     main()


# def main():
#     while True:
#         def entrada(msg):
#             try:
#                 return int (input(msg))  
#             except ValueError:
#                 print ("Digite apenas Numeros") 
                
#         n1 =  entrada('entre com um numero inteiro: ')
#         n2 =  entrada ('entre com outro numero inteiro: ')

#         # n1 =  int(input('entre com um numero inteiro: '))
#         # n2 =  int(input ('entre com outro numero inteiro: '))

#         if n1==n2==0 :
#             break

#         soma = n1+n2
#         print(f'{n1:2}  + {n2:2} = {soma:2}')

    
# if __name__ =="__main__":
#     main()
    
######################################################################    
    
# 
#         #variavel to tipo lista (mutavel/,odificado)
#     #a lista utiliza colchetes para definir os elementos    
#     lista_de_frutas = ["pera","banana","laranja","uva"]
    
#     #variavel tipo tupla (imutavel/ não poede ser alterado
#     # utiliza a parenteses para definir os elementos
#     tupla_de_cores =  ("vermelho", "azul", "verde", "amarelo")
#     fabricantesCarros = ("FIAT", "VW", "GM", "BYD")
    
#     #variavel do tipo dicionario
#     #utiliza chaves para definir sua e cave o valor
#     dicionario_de_pessoa ={
#         "nome"   : "Aline",
#         "idade"  : 25,
#         "cidade" : "Sao Paulo",
#         "cpf"    : 1234567890
#     }
    
#     #exibindo os valors da variaveis
    
#     print ("minha Lista de Futas", lista_de_frutas)
#     print (f'Tupla de cores: {tupla_de_cores}')
#     print (f'Dicionario de Pessoas {dicionario_de_pessoa}')
    
#     #acessar elementos especificos
#     #Lista e Tupla - acessar pelo numero de indice
#     #sempre começando pelo Zero
    
#     print(f'A segunda fruta da minha lista eh : {lista_de_frutas[1], lista_de_frutas[3]}')
#     print(f'A segunda fruta da minha typla de cores eh : {tupla_de_cores[0:3]}')
    
#     print (f'a idade de {dicionario_de_pessoa["nome"]}, é de {dicionario_de_pessoa["idade"]} ano')
    
#     lista_de_frutas[1]= "Limao"
#     print(f'A segunda fruta da minha lista eh : {lista_de_frutas[1]}')
    
#     #não permite a troca
#     # tupla_de_cores[1] = "Roxo"
#     # print(f'A segunda fruta da minha typla de cores eh : {tupla_de_cores[1]}')
    
#     dicionario_de_pessoa["nome"] = "Carlos"
#     dicionario_de_pessoa["idade"] = 55
    
#     print (f'a idade de {dicionario_de_pessoa["nome"]}, é de {dicionario_de_pessoa["idade"]}')
   
# if __name__ =="__main__":
#     main()

######################################################################
#criar um lista ce compra em python com as seguintes regras?
#é necessario um total de 5 frutas
#a primeira gruta deve custar 1
#a segunda fruta deve custar o dobro do valor da primeira 
#a terceira fruta deve custar o metade do valor da primeira
#a quarta fruta deve custar 3 vezes o valor da terceira fruta
#a quinta fruta deve custar o metade do valor da quartaprimeira
#apresentar o total dos valores

#cada fruta deve possuir uma variavel
#usar o menor quantidade possivel de variaveis
#todas as frutas e seus valores devem ser impressos no seguinte formato
########################################################################

#fruta: Nome da Fruta, Preco: R$ 0,00

#versão 01

def main():
    lista_de_frutas = ["pera   ","banana ","laranja","uva    ", "maça   "]  
    lista_de_preco = [1,0,0,0,0]
    lista_de_preco[1]=lista_de_preco[0]*2 #2
    lista_de_preco[2]=lista_de_preco[0]/2 #0,5
    lista_de_preco[3]=lista_de_preco[2]*3 #1,5
    lista_de_preco[4]=lista_de_preco[3]/2 #0,75
    print ("#"*50)
    print ("#"," "*46, "#")
    print ("#"," "*15, "Lista de Futas"," " *15,"#")
    print ("#"," "*46, "#")
    print ("#"*50)
    print ()
    Total=0
    for i in range (5):  
        print (f'Fruta : {lista_de_frutas[i]} , Preço R$ {lista_de_preco[i]:.2f}')
        Total=Total + lista_de_preco[i] 
    print ("-"*50)     
    print (f'Total : R$ {Total:.2f}')
    print ()
    print ("#"*50)
    print ("#"," "*46, "#")
    print ("#"," "*16, "Fim da lista"," " *16,"#")
    print ("#"," "*46, "#")
    print ("#"*50)    
    
    
    #versão 2    
    print ("Versão2")
    lista_de_frutas1 = ["pera   ",1,"banana ",0,"laranja",0,"uva    ",0, "maça   ",0]  
    lista_de_frutas1[3]=lista_de_frutas1[1]*2 #2
    lista_de_frutas1[5]=lista_de_frutas1[1]/2 #0,5
    lista_de_frutas1[7]=lista_de_frutas1[5]*3 #1,5
    lista_de_frutas1[9]=lista_de_frutas1[7]/2 #0,75
    
    print ("#"*50)
    print ("#"," "*46, "#")
    print ("#"," "*15, "Lista de Futas"," " *15,"#")
    print ("#"," "*46, "#")
    print ("#"*50)
    print ()
    i=0
    Total=0
    while (i<10):  
        print (f'Fruta : {lista_de_frutas1[i]} , Preço R$ {lista_de_frutas1[i+1]:.2f}')
        Total =Total + lista_de_frutas1[i+1] 
        i=i+2
    print ("-"*50)
    print (f'Total :R$ {Total:.2f}')
    print ()
    print ("#"*50)
    print ("#"," "*46, "#")
    print ("#"," "*16, "Fim da lista"," " *16,"#")
    print ("#"," "*46, "#")
    print ("#"*50)    
        
        
        
if __name__ =="__main__":
    main()