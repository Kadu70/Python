def main():

    # input () -> retornar o dado/info em formato de texto
    # a variavel nome vai receber um texto string) pelo teclado
    nome = input ("Digite seu nome: ")

    # para receber um numero é necessario converter o texto para um numero
    # para isso pode-se utilizar  a função int() quando ,for numero inteiro
    # ou float() quando for numero real
    # idade  = numero_inteiro ( texto )
    # 1. idade = input ("Digirte sua idade:")
    # 2. idade = int (idade)
    idade = int(input("Digite sua idade: "))

    altura = float(input("Digite sua altura: "))

    # quando for necessario converter um numero e texto
    # utilizamos a função str()  -> string = texto | caracter = letra
    numero = 50
    numero_texto= str(numero)
    
if __name__ == "__main__":
    main()