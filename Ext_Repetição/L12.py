"""12.	Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário
deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
o	Tabuada de 5:
o	5 X 1 = 5
o	5 X 2 = 10
o	...
o	5 X 10 = 50
"""
tabuada = float(input("Qual a tabuada você deseja? "))
for i in range(10):
    print(f'{tabuada} x {i+1} = {tabuada * (i+1)}')
