"""17.	Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou
não bissexto.
"""

ano = int(input("Entre com um Ano: "))
if ano % 4 != 0:
    print("ANO DE ",  ano , "NÃO É BISSEXTO!!!")
else:
    print("ANO DE ",  ano , "É BISSEXTO!!!")
