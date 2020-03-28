"""25.	Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
a.	"Telefonou para a vítima?"
b.	"Esteve no local do crime?"
c.	"Mora perto da vítima?"
d.	"Devia para a vítima?"
e.	"Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder
positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
 Caso contrário, ele será classificado como "Inocente".
"""
resp = -1
print("Responda ao inquerito digitando:\n   0 para NÃO.\n   1 para SIM.")
while resp < 0 or resp > 1:
    resp = int(input("Telefonou para a vitima?  "))
resultado = resp

resp = -1
while resp < 0 or resp > 1:
    resp = int(input("Esteve no local do crime?  "))
resultado += resp

resp = -1
while resp < 0 or resp > 1:
    resp = int(input("Mora perto da vítima?  "))
resultado += resp

resp = -1
while resp < 0 or resp > 1:
    resp = int(input("Devia para a vítima?  "))
resultado += resp

resp = -1
while resp < 0 or resp > 1:
    resp = int(input("Já trabalhou com a vítima?  "))
resultado += resp

if resultado < 2:
    print("Você é inocente!!! ")
elif resultado == 2:
    print("Você é um suspeito!!! ")
elif 3 <= resultado <= 4:
    print("Você é cumplice!!! ")
else:
    print("Você é o Assassino!!! ")
