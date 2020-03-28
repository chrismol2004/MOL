"""16.	Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá
pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
a.	Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir
    os demais valores, sendo encerrado;
b.	Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
c.	Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
d.	Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
"""
a = 0
while a == 0:
    a = float(input("Entre com o coeficiente X^2: "))
b = float(input("Entre com o coeficiente X^1: "))
c = float(input("Entre com o coeficiente X^0: "))

delta = b ** 2 - 4 * a * c
if delta < 0:
    print("Equação não possui raiz real: ")
else:
    print("A(s) raize(s) do polinomio", a, "x^2 + (", b, ")X + (", c, ") é(são): ")
    x2 = - (b - delta ** 0.5) / (2 * a)
    if delta > 0:
        x1 = - (b + delta ** 0.5) / (2 * a)
        print("Duas raizes reais: \n X1 =", x1, "e X2 =", x2)
    else:
        print("Duas raizes iguais: X =",x2)
