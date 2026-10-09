import os
os.system ("cls")

soma = 0
contador = 0
reposta = "s"

while reposta == "s":
    nota = float(input("Digite sua nota: "))

    soma = soma + nota
    contador += 1

    reposta = input("Deseja inserir mais uma nota ?:").lower()

media = soma / contador

print(f"Quantidade de notas: {contador}")
print(f"Média: {media}")