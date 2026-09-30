import os
os.system('cls')

while True:
    numero = int(input('Digite um número entre 0 a 10: '))
    if numero < 0 or numero > 10:
        print()
        print("o número esta invalido, tente novamente: ")
    else:
        print(f"\n o número esta entre 1 a 10, número informado: {numero}")
        break

print('=== FIM ===')