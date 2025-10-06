# Média de Três Notas
# Receba três variáveis para representar as notas de um aluno (nota1, nota2, nota3).
# Calcule as notas 
# Mostre as notas digitadas
# Logo apos, mostre a média aritmética dessas três notas.

# ===================================================

# Média Notas:

print("--- Exercício: Média de Três Notas ---")
# solicita notas ao usuario
nota1 = int (input("Digite a primeira nota (0-10): "))
while(nota1 < 0 or nota1 > 10):
    print('Nota incorreta (0-10)')
    nota1 = int (input("Digite a primeira nota (0-10): "))
    
nota2 = int (input("Digite a segunda nota: "))
while(nota2 < 0 or nota2 > 10):
    print('Nota incorreta (0-10)')
    nota2 = int (input("Digite a segunda nota (0-10): "))

nota3 = int (input("Digite a terceira nota: "))
while(nota3 < 0 or nota3 > 10):
    print('Nota incorreta (0-10)')
    nota3 = int (input("Digite a terceira nota (0-10): "))


media = (nota1 + nota2 + nota3) / 3

print(f"Notas: {nota1}, {nota2}, {nota3}")
print("-" * 30)
print(f"Média: {media:.2f}")
print("-" * 30)
