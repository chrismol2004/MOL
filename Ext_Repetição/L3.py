"""3.Faça um programa que leia e valide as seguintes informações:
a.	Nome: maior que 3 caracteres;
b.	Idade: entre 0 e 150;
c.	Salário: maior que zero;
d.	Sexo: 'f' ou 'm';
e.	Estado Civil: 's', 'c', 'v', 'd';
"""

nome = input("Entre com seu nome: ")
while len(nome) < 3:
    print("ERROR: Nome com menos de 3 caracteres")
    nome = input("Entre com seu nome: ")

idade = float(input("Entre com sua idade: "))
while idade < 0 or idade >150:
    print("ERROR: Idade não está entre 0 e 150.")
    idade = input("Entre com sua idade: ")

salario = float(input("Entre com o valor do salário: "))
while salario < 1:
    print("ERROR: O valor do salário menor que zero Idade não está entre 0 e 150.")
    salario = float(input("Entre com o valor do salário: "))

sexo = input("Entre com seu sexo: ")
while sexo != "F" and sexo != "M" and sexo != "f" and sexo != "m":
    print("ERROR: Dado inválido.")
    sexo = input("Entre com seu sexo: ")

estado_civil = input("Entre com seu estado civil: s - solteiro c - casado, v - viuvo, d - divorciado. ")
while estado_civil != "s" and estado_civil != "c" and estado_civil != "v" and estado_civil != "d":
    print("ERROR: Dado inválido.")
    estado_civil = input("Entre com seu estado civil: s - solteiro c - casado, v - viuvo, d - divorciado. ")
