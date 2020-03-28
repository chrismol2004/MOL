def maior_valor(vetor):
   """
   Função que determina qual o maior valor de uma lista.

   :param vetor: 
   :return: 
   """
tam = len(vetor)
if tam == 0:
    print("Error: Lista vazia.")
else:
    maior = vetor[0]
    i = 0
    while i < tam - 1:
        i += 1
        if maior < vetor[i]:
            maior = vetor[i]
            p = i
return p
