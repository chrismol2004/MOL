"""18.	Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos
valores.
"""
num = [30, 20, 1, 2, 5, 7, 12, 14, 17, 13, 9]

def acha_menor_maior_soma(sequencia = None):
    if sequencia is None:
        sequencia = []
        print(f'ERROR: Sequencia de números vazia {sequencia}')
    else:
        soma = 0
        maior = 0
        menor = 1000000000
        for i in sequencia:
            soma += i
            if i > maior:
                maior = i
            if menor > i:
                menor = i

        print(f'O menor número é: {menor}, o maior número é: {maior} e a soma dos números dá {soma}')

if __name__ == '__main__':
    acha_menor_maior_soma(num)