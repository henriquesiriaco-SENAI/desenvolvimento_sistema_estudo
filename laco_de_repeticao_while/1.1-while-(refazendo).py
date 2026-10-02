import os
os.system('cls')


while True:
    nota = float(input("Digite uma nota entre 0 e 10:"))
    if nota < 0 or nota > 10:
        print(f"Nota inválida. {nota}")
        print("Tente novamente")
        input('pressione qualquer tecla para continuar...')
        os.system('cls')
    else:
        print(f"Sua está entre 0 e 10: {nota}")
        break

