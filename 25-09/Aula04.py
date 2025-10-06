# Calculadora Simples 
# peca para usuario para inserir dois numeros
# calcule e mostre :
#     a soma dos dois numeros (+)
#     a diferença do primeiro pelo segundo (-)
#     o produto dos dois numeros(*)
#     a divisão do primeiro pelo segundo (resultado com 2 casa decimais) (/)
#     a divisão inteira do primeiro pelo segundo (//)
#     o resto da divisao do primeiro pelo segundo (%)
#     o primeiro numero elevado ao segundo numero(**)
# def main():
    
#     print ("#"*50)
#     print ("#"," "*46, "#")
#     print ("#"," "*15, "  Calculadora "," " *15,"#")
#     print ("#"," "*46, "#")
#     print ("#"*50)
#     print ()
    
#     try:
#         print ("_"*50)    
#         n1= float (input ("Entre com o primeiro valor "))
#         print ("_"*50)        
#         n2=  float (input ("Entre com o segundo valor "))
#         print ("_"*50)    
        
#         print(f'a soma dos dois numeros (+) = {(n1 + n2):.2f}' )
#         print ("_"*50)    
        
#         print(f'a diferença do primeiro pelo segundo (-) = {(n1 - n2):.2f}' )
#         print ("_"*50)    
        
#         print(f'o produto dos dois numeros(*) = {(n1 * n2):.2f}' )
#         print ("_"*50)    
        
#         print(f'a divisão do primeiro pelo segundo (resultado com 2 casa decimais) (/) = {(n1 / n2):.2f}' )
#         print ("_"*50)    
        
#         print(f'a divisão inteira do primeiro pelo segundo (//) = {(n1 // n2):.2f}' )
#         print ("_"*50)    
        
#         print(f'o resto da divisao do primeiro pelo segundo (%) = {(n1 % n2):.2f}' )
#         print ("_"*50)    
        
#         print(f'o primeiro numero elevado ao segundo numero(**) = {(n1 ** n2):.2f}' )
#         print ("_"*50)    
        
#     except ValueError:
#         print ("ERRO "*10)        
#         print("Invalido a entrado, use numeros.")
        
#     except ZeroDivisionError:
#         print ("ERRO "*10)  
#         print("Erro: Não pode dividir por zero!")        
        
#     print ("#"*50)
    
# if __name__ =="__main__":
#     main()

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#media de 3 nota 
#receba 3 variaveis para representar as notas de um aluno
#calcule as notas
#mostre as notas digitadas
#logo apos, mostre a media aritmetica dessas tre notas



import  Biblioteca

def main():
    Biblioteca.Titulo("Calculo da Media")
    
    print ("_"*50)             
    n1 = Biblioteca.EntradaFloat ('Entre com a nota 1: ',0,10)
    
    n2 = Biblioteca.EntradaFloat ('Entre com a nota 2: ',0,10)
    
    n3 = Biblioteca.EntradaFloat ('Entre com a nota 3: ',0,10)
    media  = (n1 + n2 + n3)/3
        
    print ("_"*50)      
    print (f'as notas : {n1:.2f}, {n2:.2f}, {n3:.2f} ')
    
    print ("_"*50)  
    print (f'Media = {media:.2f}')
    
    print ("_"*50)     
    if (media >=7):
        print ('Aprovado')
    else :
        if (media >=5):
            print ('Recuperação')
        else :
            print ('Reprovado')

if __name__ =="__main__":
    main()
    
