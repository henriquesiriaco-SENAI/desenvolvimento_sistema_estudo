from dataclasses import dataclass
import os
os.system("CLS")

@dataclass
class Cliente:
    #Nome da Variavel : tipo da Variavel
    nome: str
    idade : int

lista_clientes = []



#SOLICITANDO DADOS DE UM CLIENTE
lista_clientes.append(Cliente(nome = "Marta", idade = 30))
lista_clientes.append(Cliente(nome = "José" , idade = 48))


for client in lista_clientes:
    print(f"nome: {client.nome}")
    print(f"idade: {client.idade}")
    print('='*15)