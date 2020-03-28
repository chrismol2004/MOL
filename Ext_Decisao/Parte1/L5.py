"""5.	Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada
por aluno e apresentar:
o	A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
o	A mensagem "Reprovado", se a média for menor do que sete;
o	A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""
nota1 = float(input("Entre com a nota: "))
while nota1 < 0 or nota1 > 10:
    nota1 = float(input("ERROR:  Entre com a nota: "))

nota2 = float(input("Entre com a nota: "))
while nota1 < 0 or nota1 > 10:
    nota2 = float(input("ERROR:  Entre com a nota: "))

media = ( nota1 + nota2 ) / 2
if media == 10:
    print("O aluno foi Aprovado com distinção ")
elif media >= 7:
    print("O aluno foi Aprovado ")
else:
    print("O aluno foi Reprovado ")
