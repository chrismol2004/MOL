"""18.Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet
(em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""
tamanho = float(input("Entre com o tamanho do arquivo (MB): "))
velocidade = float(input("Entre com a velocidade da sua internet (Mbps): "))
print("Você levará para baixar o arquivo: ", (tamanho/velocidade)/60, " minutos.")
