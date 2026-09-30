import os
os.system('cls')


print('= tabuada =')
numero = int(input('digite um número: '))
print(f'seu numero foi: {numero}')

print('== soma ==')

for i in range(1,11):
    print(f'{numero} + {i} = {numero + i}')

print('\n == subtração ==')

numero = int(input('digite um número'))

for i in range(1,11):
    print(f'{numero} - {i} = {numero - i}')

print('\n == multiplicação ==')

numero = int(input('digite um número'))

for i in range(1,11):
    print(f'{numero} * {i} = {numero * i}')

print('\n == divisão ==')

numero = int(input('digite um número'))

for i in range(1,11):
    print(f'{numero} / {i} = {numero / i}')