"""9.	Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""
preco = []
i = 0
while i < 3:
    i += 1
    preco.append(float(input("Digite o preço do primeiro produto: ")))

preco.sort()
print("Ordem decrescente dos números: ", preco[:: -1])
