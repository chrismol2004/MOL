"""12.	Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que
depende do salário bruto (conforme tabela abaixo) e 10% para o INSS e que o FGTS corresponde a 11% do Salário Bruto, as
não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O

programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
o	Desconto do IR:
o	Salário Bruto até 900 (inclusive) - isento
o	Salário Bruto até 1500 (inclusive) - desconto de 5%
o	Salário Bruto até 2500 (inclusive) - desconto de 10%
o	Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.
No exemplo o valor da hora é 5 e a quantidade de hora é 220.
o	        Salário Bruto: (5 * 220)        : R$ 1100,00
o	        (-) IR (5%)                     : R$   55,00
o	        (-) INSS ( 10%)                 : R$  110,00
o	        FGTS (11%)                      : R$  121,00
o	        Total de descontos              : R$  165,00
o	        Salário Liquido                 : R$  935,00
"""


def calcula_salario(valor_hora, horas):
    salario_bruto = valor_hora * horas
    if 0 < salario_bruto <= 900:
        taxa = 0
    elif salario_bruto <= 1500:
        taxa = 5
    elif salario_bruto <= 2500:
        taxa = 10
    else:
        taxa = 20

    print("Salário Bruto (", valor_hora, "*", horas, ")  : R$ ", salario_bruto)
    print("     (-) IR (", taxa, " %)            : R$ ", round(salario_bruto * taxa / 100, 3))
    print("     (-) INSS (10%)             : R$ ", round(salario_bruto * 0.1, 3))
    print("     FGTS (11%)                 : R$ ", round(salario_bruto * 0.11, 3))
    print("     Total de descontos         : R$ ", round(salario_bruto * (taxa / 100 + 0.1), 3))
    print("     Salário Liquido            : R$ ", round(salario_bruto * (1 - taxa / 100 - 0.1), 3))


if __name__ == "__main__":
    valor = float(input("Entre com valor da hora de trabalho: "))
    hora = float(input("Entre com as horas de trabalho: "))

    calcula_salario(valor, hora)
