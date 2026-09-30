import os
import time
os.system('cls')

while True:
    print('''PORTAL SENAI

Informe o nome de "Usuário" e "Senha" ''')
    time.sleep(1)
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    if usuario == "TTT" and senha == "abuble":
        print("verificando....")
        time.sleep(1.2)
        print(f'\n Bem vindo de volta {usuario}')
        break
    else:
        print("\n Verificando....")
        time.sleep(1.1)
        print("Login ou Senha inválido")
        print("tente novamente \n")
        input("pressione uma tecla para continuar.......")
        os.system("cls")



