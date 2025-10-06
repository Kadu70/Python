def main():
    
    soma = 0
    
    print('=============SEJA BEM VINDO AO SITE=============')
    nome_inicial = str(input("Qual o seu nome? "))
    
    qtd_Aluno = int(input(f"Seja bem vindo {nome_inicial}, Qual a Quantidade de Alunos que Deseja Visualizar a Situação Escolar? "))
    
    for c in range(1,qtd_Aluno + 1):
        soma = 0
        name = str(input(f'Insira o nome do {c}º Aluno: '))
        for n in range(1,3):
            nota = float(input(f'Insira a {n}ª Nota do Aluno {name}: '))
            while (nota < 0 or nota > 10):
                if (nota < 0):
                    nota = float(input(f'Insira uma nota MAIOR que 0\nDigite outro valor: '))
                else:
                    nota = float(input(f'Insira uma nota MENOR que 10\nDigite outro valor: '))
            soma = nota + soma
            media = soma/2
        print(f'A Media das Notas informadas de {name} é equivalente a: {media:.2f}')
        
        if (media >= 7 and media <=10):
            print(f'O aluno {name} esta Reprovado!')
        else:
            print(f'O aluno {name} esta Reprovado!')
        
if __name__ == "__main__":
    main()