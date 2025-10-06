def pedir_nota(numero_nota):
    while True:
        try:
            nota = int(input(f"Digite a {numero_nota} nota (0-10): "))
            if 0 <= nota <= 10:
                return nota  # Retorna a nota válida e sai da função
            else:
                print('Nota deve estar entre 0 e 10.')
        except ValueError:
            print('Entrada inválida. Digite apenas números inteiros.')

# Solicita notas ao usuário usando a função
nota1 = pedir_nota("primeira")
nota2 = pedir_nota("segunda")
nota3 = pedir_nota("terceira")

# Calcula a média
media = (nota1 + nota2 + nota3) / 3

print(f"\nNotas: {nota1}, {nota2}, {nota3}")
print("-" * 30)
print(f"Média: {media:.2f}")
print("-" * 30)
