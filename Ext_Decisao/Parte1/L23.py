"""23.	Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de
arredondamento.
"""
def decimal(num):
    if num % 1:
        return 1
    else:
        return 0

if __name__ == "__main__":

    numero = float(input("Entre com um número qualquer: "))
    if decimal(numero):
        print("O numero", numero, " é decimal.")
    else:
        print("O numero", numero, " é inteiro.")
