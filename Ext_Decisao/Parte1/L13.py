"""13.	Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se
digitar outro valor deve aparecer valor inválido.
"""

calendario = {1: "Domingo", 2: "Segunda", 3: "Terça", 4: "Quarta", 5: "Quinta", 6: "Sexta", 7: "Sábado"}

num = int(input("Entre com o dia da semana: \n1 - Domingo\n2 - Segunda\n3 - Terça\n4 - Quarta\n5 - Quinta\n6 - Sexta,\n7 - Sábado.\nOpção: >> "))

if calendario.get(num,0):
    print("Hoje é ", calendario[num])
else:
    print("Valor digitado é inválido.")
