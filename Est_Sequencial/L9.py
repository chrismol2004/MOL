"""9.	Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
C = (5 * (F-32) / 9)."""

farenheit = float(input("Digite a temperatura: "))
print("A temperatura me Celsius é: ", round(5 / 9 * (farenheit-32), 2))
