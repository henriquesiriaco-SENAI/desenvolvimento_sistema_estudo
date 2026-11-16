import os
from datetime import date
os.system("cls")
ano_atual = date.today().year

def velhice(nascimento):
    resultado = ano_atual - nascimento
    return resultado

nascimento = int(input("Digite seu ano de nascimento: "))

resultado = velhice(nascimento)

print(f"Ano Atual: {ano_atual}")
print(f"Nascimento: {nascimento}")
print(f"Sua idade: {resultado}")