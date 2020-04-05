"""14.	Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade
de números impares.
"""
quant = 10
pares = []
impares = []
for i in range(quant):
    num = float(input(f'Entre com o {i+1} número: '))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

pares.sort()
impares.sort()
print(f'Os números pares são {pares} e os impares são {impares}')