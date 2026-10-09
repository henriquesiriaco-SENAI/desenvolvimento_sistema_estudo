import os
os.system("cls")

soma = 0
quantidade_notas = 0

while True:
    os.system("cls")
    print('''
==== MENU ===
s - inserir uma nota
n - calcular  média aritimética
''')

    reposta = input("Deseja inseir uma nota?").lower()

    match reposta:
        case "s":
            nota = float(input("Digite uma nota"))
            soma += nota
            quantidade_notas += 1
        case "n":
            if quantidade_notas == 0:
                print ()
                break
            else:
                break
        case _:
            print("Opção invalida \n")
            input("Pressione uma tecla para continuar ...")

if quantidade_notas == 0:
    print ("Não foi inserido as notas")
else:
    media = soma / quantidade_notas
    print(f"Média: {media}")