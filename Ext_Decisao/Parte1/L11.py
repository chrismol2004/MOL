"""11.	As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para
desenvolver o programa que calculará os reajustes.
o	Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário
 atual:
o	salários até R$ 280,00 (incluindo) : aumento de 20%
o	salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
o	salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
o	salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o	o salário antes do reajuste;
o	o percentual de aumento aplicado;
o	o valor do aumento;
o	o novo salário, após o aumento.
"""
salario_antes = float(input("Digite o valor do salário: "))
if 0 < salario_antes <= 280.00:
    taxa = 0.20
elif salario_antes <= 700.00:
    taxa = 0.15
elif salario_antes <= 1500.00:
    taxa = 0.10
else:
    taxa = 0.05
acrescimo = salario_antes * taxa

print("Salário anterior: R$ ", salario_antes)
print("O percentual de aumento: ", taxa * 100, "%.")
print("Valor do aumento: ", acrescimo)
print("Salario atual: ", salario_antes + acrescimo)
