"""15.	A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a
série até o n−ésimo termo.
"""
termo = int(input("Entre com o termo da série de fibonacci: "))
serie = []
if termo >= 1:
    serie.append(1)
    if termo >= 2:
        serie.append(1)
        for i in range(termo-2):
            serie.append(serie[i]+serie[i+1])
else:
    print('ERROR: Não tem série de Fibonacci!!!')

print(f'A série até o termo {termo} é: {serie}')