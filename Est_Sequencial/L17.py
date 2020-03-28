"""17.Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas
de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
o	Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
o	comprar apenas latas de 18 litros;
o	comprar apenas galões de 3,6 litros;
o	misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os valores
para cima, isto é, considere latas cheias.
"""
area_pintar = float(input("Entre com a área a ser pintada: "))
if area_pintar > 0:
    litros = area_pintar / 6 * 1.1
    print(">> Você vai usar ", round(litros, 2), " Litros de tinta. Logo:")
    latas_f = litros / 18
    latas_i = round(latas_f)
    galoes_f = litros/3.6
    galoes_i = round(galoes_f)
    if (latas_f - latas_i) > 0:
        latas = latas_i + 1
    else:
        latas = latas_i

    if (galoes_f - galoes_i) > 0:
        galoes = galoes_i + 1
    else:
        galoes = galoes_i

    print(">> Você deve comprar: ", latas, " Latas de tinta e pagar R$", round(latas * 80.00, 2), "ou ")
    print(">> Você deve comprar: ", galoes, " galoes de tinta e pagar R$", round(galoes * 25.00, 2), "ou ")

    latas = latas_i
    galoes_f = latas_f - latas_i / 3.6
    galoes_i = round(galoes_f)

    if (galoes_f - galoes_i) > 0:
        galoes = galoes_i + 1
    else:
        galoes = galoes_i

    print(">> Você deve comprar: ", latas, " Latas e ", galoes, " galoes de tinta e pagar R$",
          round(latas * 80 + galoes * 25, 2))
