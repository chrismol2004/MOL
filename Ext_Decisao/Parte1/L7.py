"""7.	Faça um Programa que leia três números e mostre o maior e o menor deles.
"""

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo  número: "))
num3 = float(input("Digite o terceiro número: "))
menor = -1
maior = -1
if num1 > num2:
    if num2 > num3:
        maior = num1
        menor = num3
    else:
        menor = num2
        if num1 > num3:
             maior = num1
        else:
             maior = num3
else:
    if num2 > num3:
        maior = num2
        if num1 > num3:
            menor = num3
        else:
            menor = num1
    else:
        maior = num3
        menor = num1

print("O maior número entre ", num1, num2, num3, "é: ", maior)
