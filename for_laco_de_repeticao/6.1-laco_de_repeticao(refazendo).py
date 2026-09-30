import os
os.system('cls')

print("==== LET'S LARP ====")

soma = 0

print(f"o valor Incial da variável soma: {soma}")

for i in range(3):
    numero = int(input('\nDigite um número para somar:'))
    soma += numero
    print(f"Valor da variavel Soma: {soma}")

print(f"\no valor final da variável soma: {soma}")
