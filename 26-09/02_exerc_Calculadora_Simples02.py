def main():
    
    soma = 0
    mult = 1
    sub = 0
    div = 1
    
    print ('===========SOFTWARE DE CALCULOS===========')
    name = str(input('Para iniciar, me informe o seu nome: '))
    
    print (f'{name}, Seja bem vindo ao Sistema\n')
    func = int(input(f'Qual Operação deseja realizar hoje:\n 1 - SOMA\n 2 - SUBTRAÇÃO\n 3 - MULTIPLICAÇÃO\n 4 - DIVISÃO DECIMAL\n 5 - DIVISÃO INTEIRA\n 6 - RESTO DA DIVISÃO\n 7 - ELEVAÇÃO\nOpção: '))
    
    if (func == 1):
        print(f'Digite dois números e descubra sua SOMA!')
        for c in range (1,3):
            num = float(input ('Digite o {}º Numero: ' .format(c)))
            soma = soma + num
        print(f'O Resultado da soma dos numeros é: {soma}')
            
    elif (func == 2):
        print(f'Digite dois números e descubra sua SUBTRAÇÃO!')
        for c in range (1,3):
            num = float(input('Digite o {}º Numero: ' .format(c)))
            sub = (- num - sub)
        print(f'O Resultado da Subtração dos numeros é: {sub}')
            
    elif (func == 3):
        print(f'Digite dois números e descubra sua MULTIPLICAÇÃO!')
        for c in range (1,3):
            num = float(input ('Digite o {}º Numero: ' .format(c)))
            mult = (mult * num)
        print(f'O Resultado da Multiplicação dos numeros é: {mult}')
            
    elif (func == 4):
        print(f'Digite dois números e descubra sua DIVISÃO!')
        num1 = int(input('Digite o 1º Numero: ')) 
        num2 = int(input('Digite o 2º Numero: '))
        div = num1 / num2
        print(f'O Resultado da Divisão dos numeros é: {div:.2f}')
        
    elif (func == 5):
        print(f'Digite dois números e descubra sua DIVISÃO INTEIRA!')
        num1 = int(input('Digite o 1º Numero: '))
        num2 = int(input('Digite o 2º Numero: '))
        div = num1 // num2
        print(f'O Resultado da Divisão Inteira dos numeros é: {div}')
        
    elif (func == 6):
        print(f'Digite dois números e descubra o RESTO!')
        num1 = int(input('Digite o 1º Numero: '))
        num2 = int(input('Digite o 2º Numero: '))
        rest = num1 % num2
        print(f'O Resultado do Restante dos numeros é: {rest}')
        
    elif (func == 7):
        print(f'Digite dois números e descubra o EXPONENCIAÇÃO!')
        num1 = int(input('Digite o 1º Numero: '))
        num2 = int(input('Digite o 2º Numero: '))
        expo = num1 ** num2
        print(f'O Resultado da Exponenciação dos numeros é: {expo}')
        
    else:
        print('ERRO!!')   
    
if __name__ == "__main__":
    main()    