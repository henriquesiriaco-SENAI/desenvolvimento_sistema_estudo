import os
os.system('cls')

QUANTIDADE_NOTAS = 4
soma_notas = 0.0

for i in range(QUANTIDADE_NOTAS):
    soma_notas += float(input('digite sua nota'))

media = soma_notas / QUANTIDADE_NOTAS

print('\n ==== Exibindo resultado ====')
print(f'Media: {media}')
print(" Fim ")