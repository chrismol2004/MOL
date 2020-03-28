"""15.	Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um
triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno
o	Dicas:
o	Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
o	Triângulo Equilátero: três lados iguais;
o	Triângulo Isósceles: quaisquer dois lados iguais;
o	Triângulo Escaleno: três lados diferentes;
"""
i = 0
triangulo = {1: "Equilatero", 2: "Isoceles", 3: "Escaleno"}
n_lados = {}
while i < 3:
    i += 1
    lado = float(input("Entre com um lado do triângulo: "))
    num = n_lados.get(lado, 0)
    if num:
        pass
    else:
        n_lados[lado] = i

num = n_lados.__len__()
print("O triângulo é ", triangulo.get(num, 0))
