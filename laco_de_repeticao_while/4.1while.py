import os
os.system("cls")

login_salvo = "casa"
senha_salva = "123"
tentativas = 1

while True:
    if tentativas <= 3:
        print(f"Tentativa: {tentativas}")
        login = input ('Digite o Login')
        senha = input ('Digite a senha')
        tentativas +=1

        if login == login_salvo and senha == senha_salva:
            print('bem-vindo!')
            break
        else:
            print("\n login ou senha invalida")
            print("tente novamente \n")
            input("presscione qualquer tecla para continuar...")
            os.system('cls')
    else:
        print("= FIM -")
        break