import os
os.system("cls")
def inflacionar_preco(preco_produto):
    if preco_produto >= 100:
        resultado = preco_produto * 1.20
    else:
        resultado = preco_produto * 1.10
    return resultado



print("== SOLICITANDO DADOS ==")
preco_produto = float(input("Digite o seu preço: "))

#chamado a função
preco_inflacionado = inflacionar_preco(preco_produto)


print("\n== Exibindo Dado ==")
print(f"preço inicial: {preco_produto}")
print(f"preço inflacionado: {preco_inflacionado}")