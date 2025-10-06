print("--- Exercício: Média de Três Notas ---")

# solicita notas ao usuario
#
#  - while True: 
#     * loop infinito que só será quebrado quando uma 
#       entrada válida for fornecida.
#  - Instrução try 
#     * usada para envolver um bloco de código 
#       que pode gerar um erro (exceção)
#  - O try pode ser interrompido e o controle
#    é passado para um ou mais blocos except, 
#    onde o erro pode ser tratado

while True:
    try:
        nota1 = int(input("Digite a primeira nota (0-10): "))
        if 0 <= nota1 <= 10:
            break  # Sai do loop se a nota for válida
        else:
            print('Nota deve estar entre 0 e 10.')
    except ValueError:
        print('Entrada inválida. Digite apenas números inteiros.')
        
while True:
    try:
        nota2 = int(input("Digite a segunda nota (0-10): "))
        if 0 <= nota2 <= 10:
            break  # Sai do loop se a nota for válida
        else:
            print('Nota deve estar entre 0 e 10.')
    except ValueError:
        print('Entrada inválida. Digite apenas números inteiros.')
        
while True:
    try:
        nota3 = int(input("Digite a terceira nota (0-10): "))
        if 0 <= nota3 <= 10:
            break  # Sai do loop se a nota for válida
        else:
            print('Nota deve estar entre 0 e 10.')
        
    except ValueError:
        print('Entrada inválida. Digite apenas números inteiros.')
    

media = (nota1 + nota2 + nota3) / 3

print(f"Notas: {nota1}, {nota2}, {nota3}")
print("-" * 30)
print(f"Média: {media:.2f}")
print("-" * 30)
