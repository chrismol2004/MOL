"""8.	Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre
o total do seu salário no referido mês.
"""

salario_hora = float(input("Digite o valor da hora trabalhada: "))
horas_trabalho = float(input("Digite o número de horas trabalhadas: "))

print("Você ganha no mês: R$", round(salario_hora*horas_trabalho), 2)
