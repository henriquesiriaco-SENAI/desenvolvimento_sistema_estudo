import os
os.system("cls")

soma_pare = 0
contador_pares = 0
soma_geral = 0
contador_geral = 0
contador_impares = 0

while True:
    numero = int(input("Digite seu número"))
    if numero == 0:
        break
    soma_geral += 1
    if numero % 2 == 0:
        contador_pares += 1
        soma_pare += numero
    else:
        contador_impares += 1
        print(f"Números pare {contador_pares}")
        print(f"Número impares {contador_impares}")
    if contador_pares > 0:
        media_pares = soma_pare /contador_pares
        print(f"Media pares: {media_pares}")

    else:
        print("Sem valor")
    if contador_geral > 0:
            media_geral = soma_geral / contador_geral
            print(f"média geral: {media_geral}")
    else:
        print("Sem valor")