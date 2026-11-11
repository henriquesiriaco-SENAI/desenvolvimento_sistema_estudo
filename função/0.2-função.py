import os
os.system("cls")

def mostrar_saudacao(nome, idade):
    print(f"{nome} tem {idade} anos")


print('Solicitando dados=')
nome = input(' Digite o seu nome: ')
idade = input(' Digite o seu idade: ')


print('\n= Exibindo dados=')
mostrar_saudacao(nome, idade)