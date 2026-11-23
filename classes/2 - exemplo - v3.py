from dataclasses import dataclass
import os
os.system("cls")

@dataclass
class Cliente:
    nome : str
    telefone : str
    email : str

    #função dentro do class
    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Telefone: {self.telefone}")
        print(f"Email: {self.email}")
        print("="* 30)
    #função somente para enviar e-mails
    def emails_marketing(self):
        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}")
        print("="* 30)
    def whatsapp_marketing(self):
        print(f"Nome: {self.nome}")
        print(f"Telefone: {self.telefone}")
        print("="* 30)

lista_cliente = []

print(" = SOLICITANDO DADOS =")
for i in range(1):
    dados_cliente = Cliente(
            nome = input("Digite o nome do cliente: "),
            telefone =input("Digite o número do Cliente:"),
            email = input("Digite o email do cliente: ")
        )
    lista_cliente.append(dados_cliente)

print("\n === EXIBINDO DADOS ===")
for client in lista_cliente:
    client.mostrar_dados()
print("\n === EXIBINDO EMAIL MARKETING ===")
for client in lista_cliente:
    client.emails_marketing()


for client in lista_cliente:
    client.whatsapp_marketing()