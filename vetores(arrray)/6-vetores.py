import os
os.system("cls")



print("= INSERINDO NÚMEROS NO VETOR =")
vetor_numeros = []
for i in range(5):
    livro = input(f"Me fale do {i + 1}°  livro: ")
    vetor_numeros.append(livro)

print ("\n= EXIBINDO NÚMEROS DO VETOR =")
for indice, livro in enumerate (vetor_numeros,start=1): #forEach
    print(f"{indice}°: {livro}")