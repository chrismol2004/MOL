"""2.Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando
uma mensagem de erro e voltando a pedir as informações.
"""
nome = input("Entre com o Usuário: ")
senha = input("Entre com uma senha: ")
nome = nome.lower()
senha = senha.lower()
while nome == senha:
    print("ERROR: Senha igual ao nome, inválida.")
    senha = input("Entre com uma senha diferente do nome: ")
    senha = senha.lower()

print("Cadastro efetivado")