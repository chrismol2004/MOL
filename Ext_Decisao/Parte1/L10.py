"""10.	Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou
N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
"""
opcoes = { 'M': "Bom Dia!", 'V': "Boa Tarde!", 'N': "Boa Noite!", 'm': "Bom Dia!", 'v': "Boa Tarde!", 'n': "Boa Noite!" }
turno = input("Em que turno você estuda: \n  M-matutino \n  V-Vespertino ou \n  N- Noturno. \n  opcao: ")
if opcoes.get(turno):
    print(opcoes[turno])
else:
    print("Valor Inválido!")
