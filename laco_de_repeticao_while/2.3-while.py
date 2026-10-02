import os
os.system('cls')

QUANTIDADE_NOTAS = 2
soma = 0

for i in range (QUANTIDADE_NOTAS):
    while True:
        numero = int(input(f'Digite a {i + 1}° nota, entre 0 e 10:  '))
        if numero < 0 or numero > 10:
            print(f"Número sugerido foi incorreto: {numero}")
            print('tente novamente')
            input('pressione para continuar...')
            os.system('cls')
        else:
            soma += numero
            break

media = soma / QUANTIDADE_NOTAS

print(f"sua nota total: {soma}")
print(f"Média {media}")
print("=== FIM ===")