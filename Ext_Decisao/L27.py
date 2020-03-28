"""27.	Uma fruteiria está vendendo frutas com a seguinte tabela de preços:
o	                      Até 5 Kg           Acima de 5 Kg
o	Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
o	Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto
de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças
adquiridas e escreva o valor a ser pago pelo cliente.
"""
maca = float(input("Entre com a quantidade(em Kg) de macas: "))
morango = float(input("Entre com a quantidade(em Kg) de morangos: "))
preco = 0

if 0 <= maca <= 5:
    p_maca = 1.80
    p_morango = 2.50
else:
    p_maca = 1.50
    p_morango = 2.20

preco = p_maca*maca + p_morango*morango

if preco > 25.00 or preco > 25.00:
    preco = preco - preco*0.01

print('O valor a ser pago por ', maca, "macas e ", morango, 'morangos é ', preco)