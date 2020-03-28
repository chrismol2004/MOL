"""24.Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O
resultado da operação deve ser acompanhado de uma frase que diga se o número é:
a.	par ou ímpar;
b.	positivo ou negativo;
c.	inteiro ou decimal.
"""
from Ext_Decisao.Parte1.L23 import decimal
from Ext_Decisao.Parte1.L2 import positivo
resultado = {"000": "par, negativo e inteiro", "001": "par, negativo e decimal", "010": "par, positivo e inteiro",
             "011": "par, positivo e decimal", "100": "impar, negativo e inteiro", "101": "impar, negativo e decimal",
             "110": "impar, positivo e inteiro", "111": "impar, positivo e decimal"}

numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite outro número: "))
oper = input("Digite a operação:\n+ soma.\n- subtraçãõ.\n* multiplicação.\n/ divisão.\n^ potência. \nV raiz.\n>>")
numero = -1
if oper == "+":
    numero = numero1 + numero2
elif oper == "-":
    numero = numero1 - numero2
elif oper == "*":
    numero = numero1 * numero2
elif oper == "/":
    numero = numero1 / numero2
elif oper == "^":
    numero = numero1 ** numero2
elif oper == "V":
    numero = numero2 ** (1/numero1)
resp = ""

n = int(numero % 2)
resp += str(n) + str(positivo(numero)) + str(decimal(numero))
print("O número", numero, " é ", resultado[resp])
