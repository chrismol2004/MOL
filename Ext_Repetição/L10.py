"""10.	Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido
 por eles.
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

print(f'Os números são: {num} ')
