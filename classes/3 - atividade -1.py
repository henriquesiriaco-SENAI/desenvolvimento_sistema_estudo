from dataclasses import dataclass
import os
os.system("cls")

@dataclass
class Cliente:
    nome : str
    idade : int
    telefone : str
    endereco : str
    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Telefone: {self.telefone}")
        print(f"Endereço: {self.endereco}")
        print("="*30)

    def pessoa_marketing(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print("="*30)

    def morada_marketing(self):
        print(f"Nome: {self.nome}")
        print(f"Telefone: {self.telefone}")
        print("="*30)

lista_dados = []

for i in range(2):
    print("--- SOLICITANDO DADOS ---")
    dados_cliente = Cliente(
        nome = input("Digite o seu Nome: "),
        idade = int(input("Digite a sua idade: ")),
        telefone = input("Digite o seu telefone: "),
        endereco = input("Digite o seu endereco: ")
    )
    lista_dados.append(dados_cliente)


print("--- EXIBINDO DADOS ---")
for client in lista_dados:
    client.mostrar_dados()

print("--- NOME E IDADE ---")
for client in lista_dados:
    client.pessoa_marketing()

print("--- NOME E TELEFONE ---")
for client in lista_dados:
    client.morada_marketing()