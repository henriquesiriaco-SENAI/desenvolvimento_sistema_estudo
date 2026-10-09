import os
os.system ("cls")

soma = 0
contador = 0

while True:
    valor = int(input("Digite um valor : "))
    if valor < 0:
        break
    soma += valor
    contador += 1
    media = soma / contador
    if contador > 0:
        print(f"A media é {media}")
    else:
        print("Nenhum valor positivo inserido")