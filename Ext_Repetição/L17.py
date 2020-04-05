"""17.	Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
"""
num = int(input(f'Entre com um número inteiro: '))
fatorial = 1
operacao = f'{num}! = '

while num > 1:
    fatorial *= num
    operacao += f'{num}.'
    num -=1

operacao += f'{num} = {fatorial}'
print(operacao)