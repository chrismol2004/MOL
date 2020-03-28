"""5.	Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
Valide a entrada e permita repetir a operação.
"""
TAXA_A = 0.03
TAXA_B = 0.015

populacao_A = float(input("Entre com o número de habitantes de A: "))
while populacao_A < 0:
    populacao_A = float(input("Entre com o número de habitantes de A: "))

taxa_A = float(input("Entre com o a taxa de crescimento da populacao: "))
while taxa_A < 0:
    taxa_A = float(input("Entre com o a taxa de crescimento da populacao: "))

populacao_B = float(input("Entre com o número de habitantes de B: "))
while populacao_B < 0:
    populacao_B = float(input("Entre com o número de habitantes de B: "))

taxa_B = float(input("Entre com o a taxa de crescimento da populacao: "))
while populacao_B < 0:
    taxa_B = float(input("Entre com o a taxa de crescimento da populacao: "))

ano = 0
while populacao_A < populacao_B:
    ano += 1
    populacao_A = populacao_A * (1 + TAXA_A)
    populacao_B = populacao_B * (1 + TAXA_B)

print(f"será preciso esperar por {ano} anos. ")