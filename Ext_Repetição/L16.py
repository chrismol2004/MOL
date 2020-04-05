"""16.	A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série
até que o valor seja maior que 500.
"""
MAX = 500
i = 1
serie = []
serie.append(1)
serie.append(1)

termo = serie[i] + serie[i - 1]
while termo < MAX:
    serie.append(termo)
    i += 1
    termo = serie[i]+serie[i-1]

print(f'A série é: {serie}')