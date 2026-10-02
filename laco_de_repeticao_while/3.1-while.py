import os
import time
os.system('cls')

login_salva = input("Digite seu login: ") # "CASA" Login que eu vou atribuir
senha_salva = input("Digite sua senha: ") # "CASA" Senha que eu vou atribuir
os.system("cls")

while True:
    print('''
=== SENAI ===''')
    login = input("Escreva o seu Login: ")
    senha = input ("Escreva a sua senha: ")

    login_correto = login == login_salva
    senha_correta = senha == senha_salva

    if login_correto and senha_correta:
        print(f"Bem vindo de volta, {login_salva}")
        break
    else:
        print('Login ou senha incorreta \n tente novamente! \n ')
        time.sleep(3)
        os.system("cls")
