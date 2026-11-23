from dataclasses import dataclass
import os
os.system("CLS")

@dataclass
class Cliente:
    #Nome da Variavel : tipo da Variavel
    nome: str
    idade : int
    altura : float
    peso : float

lista_clientes = []



#SOLICITANDO DADOS DE UM CLIENTE
for i in range(2):
    dados_do_cliente = Cliente( 
        nome = input("Digite o nome do cliente: "),
        idade = int(input("Digite sua idade: ")),
        altura = float(input("Digite a sua altura: ")),
        peso = float(input("Digite o seu peso: "))
    )
    lista_clientes.append(dados_do_cliente)

print("\n ====  EXIBINDO DADOS ====")
for client in lista_clientes:
    print(f"nome: {client.nome}")
    print(f"idade: {client.idade}")
    print(f"Altura: {client.altura}")
    print(f"Peso: {client.peso}")
    print('='*15)