# import Biblioteca
# def main():
#     Biblioteca.Titulo("Desafio Logico")
#     aluno = input ('Entre com o nome do Aluno: ')
#     nota = Biblioteca.EntradaInt("entre com a Nota do Aluno (0 a 100): ", 0,100)
#     while (True):
#         freq = Biblioteca.EntradaInt("entre com a Frequencia do Aluno (0 a 100): ", 0 , 100)
#         if (freq >= 0 and freq <= 100):
#             break
#     situacao = "Aprovado"
#     if  (nota >= 90 and freq >= 60):
#         situacao = situacao + " com Bonus"
#     else:
#         if(nota < 70 or freq < 75 ):
#             situacao = "Reprovado"
#     print (f'o Aluno {aluno}, foi {situacao}, com a Nota {nota} e com {freq}% de Frequencia.')
        
#     Biblioteca.Titulo ('Fim')   
    
# if __name__ =="__main__":
#     main()
    
def main():
    while(True):
        nome = input('Digite o nome: ')
        cargo = str(input("Digite o cargo: ").strip()) #strip remove espaços extras
        depto = str(input("Digite o departamento: ").strip())
        acesso= str('Acesso Negado')
        if (cargo.upper() == 'ADMINISTRADOR' and depto.upper() == "TI"):
            acesso= 'Acesso Total'
        elif (cargo.upper() == 'GERENTE' or depto.upper() == "VENDAS"):
            acesso= 'Acesso Parcial'
        print (f'o funcionario: {nome},') 
        print (f'que tem o cargo: {cargo.capitalize()}')
        print (f'que tem o departamento: {depto.capitalize()}')
        input('continua? (0)')
        print (f', tem {acesso}')
        
        continua = int (input('continua? (0)'))
        if continua != 0 :
            break
        
if __name__ =="__main__":
    main()