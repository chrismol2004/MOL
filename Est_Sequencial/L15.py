"""15.Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre
o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5%
para o sindicato, faça um programa que nos dê:
a.	salário bruto.
b.	quanto pagou ao INSS.
c.	quanto pagou ao sindicato.
d.	o salário líquido.

calcule os descontos e o salário líquido, conforme a tabela abaixo:
    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
"""
salario_hora = float(input("Digite o valor da hora trabalhada: "))
horas_trabalho = float(input("Digite o número de horas trabalhadas: "))

salario_bruto = salario_hora * horas_trabalho
inss = 0.08 * salario_bruto
IR = 0.11 * salario_bruto
sind = 0.05 * salario_bruto
salario_liquido = salario_bruto - inss - IR - sind

print(">> Salário bruto foi de :", salario_bruto, ".")
print(">> Você pagou ao INSS: ", inss, ".")
print(">> Você pagou ao sindicato: ", sind, ".\n>> Seu salário lìquido foi: ", salario_liquido, ".")
