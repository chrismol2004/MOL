"""2.	Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
"""
def positivo(num):
    if num < 0:
        return 0
    else:
        return 1

if __name__ == "__main__":
    numero = float(input("digite um número: "))
    if positivo(numero):
        print("O número é positivo")
    else:
        print("O número é negativo")
