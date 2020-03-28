def menor_valor(vetor):
    """
    Função que determina qual o menor numero de uma lista.
    :param vetor:  lista com números
    :return p:     posição do menor elemento na lista
    """
    tam = len(vetor)
    if tam == 0:
        print("Error: Lista vazia.")
    else:
        menor = vetor[0]
        i = 0
        while i < tam-1:
            i += 1
            if menor > vetor[i]:
               menor = vetor[i]
               p = i
    return p
