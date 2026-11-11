import os
os.system("cls")

def logo_senai():
    os.system("CLS")
    print("="*15)
    print("   SENAI - BAHIA")
    print("="*15)

def mostrar_dados(nome, email, telefone):
    print(f"Seu Nome: {nome}")
    print(f"Seu email: {email}")
    print(f"Seu telefone: {telefone}")


print('Solicitando dados=')

logo_senai()
nome = input(' Digite o seu nome: ')

logo_senai()
email = input(' Digite o seu email: ')

logo_senai()
telefone = input('Digise o seu telefone:')


print('\n= Exibindo dados=')
mostrar_dados(nome, email, telefone)