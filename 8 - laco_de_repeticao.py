import os
os.system('cls')

soma = .0

for i in range (4):
    nota = float(input(f'digite sua {i+1}° nota:'))
    soma += nota
media = soma / 4
    print(f'sua soma: {soma}')


print(f'sua media {media}')
print('Fim')