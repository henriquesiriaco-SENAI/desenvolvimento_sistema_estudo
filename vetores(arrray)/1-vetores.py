import os
os.system("cls")

vetor_nome = []

for i in range(4):
    nome = input("Digite o nome do seus amigos: ")
    vetor_nome.append(nome)

for i in range(4):
    print(f"Nome {vetor_nome[i]}")