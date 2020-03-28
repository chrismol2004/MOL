"""19. Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades
do mesmo.
o	Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
o	326 = 3 centenas, 2 dezenas e 6 unidades
o	12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""
num = int(input("Entre com um número (0 < numero < 1000): "))
while num > 1000:
    print("ERROR: Número maior que 1000.")
    num = int(input("Entre com um número menor que 1000: "))

unidade = num % 10
num1 = num // 10
dezena = num1 % 10
centena = num1 // 10
if centena:
    print(">>", num, "=", centena, "centenas,", dezena, "dezenas e", unidade, "unidades")
elif dezena:
    print(">>", num, "=", dezena, "dezenas e", unidade, "unidades")
else:
    print(">>", num, "=", unidade, "unidades")
