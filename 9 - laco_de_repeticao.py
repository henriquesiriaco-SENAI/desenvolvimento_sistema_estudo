import os
import time
os.system('cls')

QUANTIDADE_NOTAS = 3
notas = 0.0

for i in range(QUANTIDADE_NOTAS):
    notas += float(input(f'Digite sua {i+1}° nota: '))

media = notas / QUANTIDADE_NOTAS

if media >= 7:
    resultado = ("Aprovado!!!! Meus parábens")
elif media >= 5:
    resultado = ("Recuperação...... É tem que estudar")
else:
    resultado = ("Reprovado, mais sorte na proxima vez")

print(f"E o reusltado foi.........")
time.sleep(2)
print(f'vejamos, sua media foi: {media}')
time.sleep(2)
print('isso significa que você foi.....')
time.sleep(3)
print('está sentindo o coração bater acelerado? kkkk')
time.sleep(2)
print('Agora sim, você foi....')
time.sleep(2)
conversa = str(input('você quer "conversa" ou quer saber da "nota"?')).lower()
if conversa == 'nota':
    print("sem graça")
    time.sleep(2)
    print(resultado)
elif conversa == 'conversa':
    print('eu não quero conversa não bobalhão')
    time.sleep(2)
    print(resultado)