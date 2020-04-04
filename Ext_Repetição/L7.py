"""7.	Faça um programa que leia 5 números e informe o maior número.
"""
quant = 5
num = []
maior = float(input("Digite um número: "))
num.append(maior)
for i in range(quant-1):
    num.append(float(input("Digite um número: ")))
    if num[i+1] > maior:
        maior = num[i+1]

print(f'O maior número digitado entre {num} é o {maior}')
