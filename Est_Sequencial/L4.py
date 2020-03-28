"""4.	Faça um Programa que peça as 4 notas bimestrais e mostre a média."""

numero = input("Entre com um número: ")
media = int(numero)
numero = input("Entre com outro número: ")
media = media + int(numero)
numero = input("Entre com outro número: ")
media = media + int(numero)
numero = input("Entre com outro número: ")
media = media + int(numero)
print("A média das notas é : ", round(media/4), 2)
