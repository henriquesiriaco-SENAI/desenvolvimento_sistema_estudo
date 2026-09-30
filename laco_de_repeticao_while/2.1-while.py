import os
os.system('cls')

QUANTIDADE_NOTAS = 2
soma = 0

for i in range(QUANTIDADE_NOTAS):
    while True:
        nota = float(int(input(f'Digite sua {i + 1}° nota, entre 0 a 10: ')))
        if nota < 0 or nota > 10:
            print()
            print('Número errado, digite novamente')
        else:
            soma += nota
            break

media = soma / QUANTIDADE_NOTAS

print(f'sua média: {media}')
print('=== FIM ===')
