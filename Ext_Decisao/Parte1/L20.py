"""20.	Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por
aluno e presentar:
a.	A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
b.	A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
c.	A mensagem "Aprovado com Distinção", se a média for igual a 10.
"""


def calcula_media(vet):
    soma = 0
    for elem in vet:
        soma = soma + elem
    media = soma / len(vet)
    if media == 10:
        print("O aluno foi Aprovado com distinção!!! Sua média foi: ", round(media, 2,))
    elif media >= 7:
        print("O aluno foi Aprovado!!! Sua média foi: ", round(media, 2,))
    else:
        print("O aluno foi Reprovado!!! Sua média foi: ", round(media, 2,))
    exit()


if __name__ == "__main__":
    nota = [-1, - 1, - 1]
    i = 0
    while i < 3:
        nota[i] = float(input("Entre com a nota do aluno: "))
        if nota[i] < 0 or nota[i] > 10:
            print("ERROR: Nota invalida: ")
        else:
            i += 1

    calcula_media(nota)
