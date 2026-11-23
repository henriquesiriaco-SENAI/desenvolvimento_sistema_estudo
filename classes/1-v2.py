from dataclasses import dataclass
import os
os.system("CLS")

@dataclass
class Cliente:
    #Nome da Variavel : tipo da Variavel
    nome: str
    idade : int


#SOLICITANDO DADOS DE UM CLIENTE
cliente1 = Cliente("Marta" , 30)
cliente1 = Cliente("Marta" , 30)



#SOLICITANDO DADOS DE OUTRO CLIENTE
cliente2 = Cliente("Marta" , 30)

print(f"Nome: {cliente1.nome}")
print(f"Idade: {cliente1.idade}")

print(f"Nome: {cliente2.nome}")
print(f"Idade: {cliente2.idade}")