"""28.	O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
o	                      Até 5 Kg           Acima de 5 Kg
o	File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
o	Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
o	Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há
limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um
desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo
usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de
pagamento, valor do desconto e valor a pagar.
"""
preco_abaixo_5 = {"F": 4.90, "A": 5.90, "P": 6.90, "f": 4.90, "a": 5.90, "p": 6.90}
preco_acima_5 = {"F": 5.80, "A": 6.80, "P": 7.80, "f": 5.80, "a": 6.80, "p": 7.80}
tipo_de_carne = {"F": "File Duplo", "A": "Alcatra", "P": "Picanha", "f": "File Duplo", "a": "Alcatra", "p": "Picanha"}
tipo = input("Entre com o tipo de carne: \nF - File Duplo. \nA - Alcatra. \nP - Picanha ")
carne = float(input("Entre com a quantidae de carne: "))
pagamento = input("Forma de pagamento: \nC - cartão tabajara\nD - dinheiro.")

if carne <= 5:
    conta = preco_abaixo_5[tipo] * carne
else:
    conta = preco_acima_5[tipo] * carne

print(f'Cupom Fiscal\nProduto: {tipo_de_carne[tipo]} \nQuantidade: {carne} \nValor: {conta}')

if pagamento == "C" or pagamento == 'c':
    print(f'desconto: {conta*0.05}')
    conta = conta * 0.95
    print(f'TOTAL: {conta}')
