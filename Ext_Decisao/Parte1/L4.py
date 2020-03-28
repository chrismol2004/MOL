"""4.	Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""
vogais = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5, 'A': 6, 'E': 7, 'I': 8, 'O': 9, 'U': 10, }
consoantes = {'b': 1, 'c': 2, 'd': 3, 'f': 4, 'g': 5, 'h': 6, 'j': 7, 'k': 8, 'l': 9, 'm': 10, 'n': 11, 'p': 12, 'q': 13, 'r': 14, 's': 15, 't': 16, 'v': 17, 'w': 18, 'x': 19, 'y': 20, 'z': 21 ,'ç': 22,}

letra = input("Digite uma letra: ")

if vogais.get(letra, 0):
    print("A letra é uma vogal")
elif consoantes.get(letra, 0):
    print("A letra é uma consoante")
else:
    print("A letra não é vogal ou consoante")