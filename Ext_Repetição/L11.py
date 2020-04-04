"""11.	Altere o programa anterior para mostrar no final a soma dos números.
"""
maior = float(input("Digite um número: "))
menor = float(input("Digite um número: "))
num = []
if menor > maior:
    aux = maior
    maior = menor
    menor = aux

while menor <= maior:
    num.append(menor)
    menor+=1

soma = 0
quant = len(num)
for i in range(quant):
    soma += num[i]




print(f'Os numeros são: {num} e o somatório é: {soma}')
