"""26.	Um posto está vendendo combustíveis com a seguinte tabela de descontos:
a.	Álcool:
	    até 20 litros, desconto de 3% por litro
        acima de 20 litros, desconto de 5% por litro
d.	Gasolina:
        até 20 litros, desconto de 4% por litro
        acima de 20 litros, desconto de 6% por litro.
Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma:
A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é
R$ 2,50 o preço do litro do álcool é R$ 1,90.
"""
litros = float(input("Entre com a quantidade de Litros: "))
tipo = input("o tipo de combustível (A-álcool, G-gasolina)")
preco = {'A': 1.9, 'B': 2.50}
if tipo == 'A':
    if litros <= 20:
        desc = 0.03
    else:
        desc = 0.05
else:
    preco = 2.50
    if litros <= 20:
        desc = 0.04
    else:
        desc = 0.06

print("O valor de ", litros, "Litros de combustível é :", preco[tipo]*litros*(1+desc))
