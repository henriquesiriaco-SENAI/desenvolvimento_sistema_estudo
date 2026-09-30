import os
os.system('cls')

TENTATIVAS = 3

for i in range(TENTATIVAS):
    print(f"tentativa: {i+1}")
    login = input('Login: ')
    senha = input("Senha: ")
    if login == "ca" and senha == "sa":
        print("Bem vindo")
        break
    else:
        print("login ou senha invalidos!")
        print("Tente novamente")
        input('Digite para continuar.....')
        os.system("cls")

print('=== Fim ===')