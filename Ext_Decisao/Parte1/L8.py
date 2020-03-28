"""8.	Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a
decisão é sempre pelo mais barato.
"""
from Ext_Decisao.Menor import menor_valor
preco = []
i = 0
while i < 3:
    i += 1
    preco.append(float(input("Digite o preço do primeiro produto: ")))

posicao = menor_valor(preco)

print("Você deve comprar o ", posicao + 1, "produto que custa R$", preco[posicao])
