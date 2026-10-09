import os
import time


soma_pares = 0
soma_geral = 0
quantidade_numeros = 0
quantidade_pares = 0
quantidade_impares = 0

while True:
    os.system("cls")
    numero = int(input("Digite um Número: "))

    if numero >= 0:
        quantidade_numeros += 1
        soma_geral += numero

        if numero % 2 == 0:
            quantidade_pares +=1
            soma_pares += numero  
        else:
            quantidade_impares +=1
            time.sleep(1)
    else:
        break

if quantidade_numeros == 0:
    print("Não foi possivel calcular \n")
else:
    media_geral = soma_pares / quantidade_numeros
    media_pares = soma_pares / quantidade_pares

    print (f"Média geral: {media_geral}")
    print(f"media pares {media_pares}")
    print(f"quantidade de pares {quantidade_pares}")
    print(f"quantidade de impares {quantidade_impares}")