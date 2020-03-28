"""11.	Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
a.	o produto do dobro do primeiro com metade do segundo .
b.	a soma do triplo do primeiro com o terceiro.
c.	o terceiro elevado ao cubo.
"""
num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))
num3 = float(input("Digite um número real: "))

print("O produto do dobro do primeiro com metade do segundo é:", num1 * 2 * num2 / 2)
print("A soma do triplo do primeiro com o terceiro", 3 * num1 + num3)
print("O terceiro elevado ao cubo", num3 ** 3)
