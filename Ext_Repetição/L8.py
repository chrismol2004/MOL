"""8.	Faça um programa que leia 5 números e informe a soma e a média dos números.
"""
quant = 5
num = []
soma = float(input("Digite um número: "))
num.append(soma)
for i in range(quant-1):
    num.append(float(input("Digite um número: ")))
    soma += num[i+1]

print(f'A soma dos números {num} é: {soma}  e a sua média é: {soma/quant}')