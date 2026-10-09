import os
import time
os.system("cls")

soma = 0
quantidade_notas =0

while True:
    os.system("cls")
    numero = int(input("Digite um número: "))

    if numero >= 0:
        soma += numero
        quantidade_notas += 1
        time.sleep(0.5)
    else:
        break

if quantidade_notas == 0:
    print("Não foram inseridos número \n")
else:
    media = soma  /quantidade_notas
    print(f"media: {media}")