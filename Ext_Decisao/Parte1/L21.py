"""21.	Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois
informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O
valor mínimo é de 10 reais e o máximo de 600 reais. Não se preocupe com a quantidade de notas existentes na máquina.
a.	Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e
    uma nota de 1;
b.	Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de
    10, uma nota de 5 e quatro notas de 1.
"""
saque = 0
while not 10 <= saque <= 600:
    saque = int(input("Entre com o valor a ser sacado (de 10 a 600 reais): "))

if saque >= 100:
    print("Será fornecido: ", round(saque // 100), "notas de 100 reais.")
    saque = saque % 100

if saque >= 50:
    print("Será fornecido: ", round(saque // 50), "notas de  50 reais.")
    saque = saque % 50

if saque >= 10:
    print("Será fornecido: ", round(saque // 10), "notas de  10 reais.")
    saque = saque % 10

if saque >= 5:
    print("Será fornecido: ", saque // 5, "notas de   5 reais.")
    saque = saque % 5

if saque >= 2:
    print("Será fornecido: ", saque // 2, "notas de   2 reais.")
    saque = saque % 2

if saque >= 1:
    print("Será fornecido: ", saque, "notas de   1 reais.")
