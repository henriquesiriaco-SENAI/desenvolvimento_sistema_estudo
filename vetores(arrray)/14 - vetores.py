import os
os.system("cls")

vetor_comida = []
picanha = 25
lasanha = 20
strongonoff = 18
bife_acebolado = 15
pao_c_ovo = 5

while True:
    os.system("cls")
    print('''
1 - Picanha        R$ 25,00
2 - Lasanha        R$ 20,00
3 - Strongonoff    R$ 18,00
4 - Bife Acebolado R$ 15,00
5 - Pão com ovo    R$ 5,00''')
    pedido = int(input("Qual prato deseja? 1/2/3/4/5?"))
    match pedido:
        case 1:
            print(f"Prato Selecionado Picanha, valor: {picanha}")
            vetor_comida.append(25)
            repetir = input("Deseja outro pedido? ").upper()
            if repetir == "N":
                break
        case 2:
            print(f"Prato Selecionado Picanha, valor: {lasanha}")
            vetor_comida.append(20)
            repetir = input("Deseja outro pedido? ").upper()
            if repetir == "N":
                break
        case 3:
            print(f"Prato Selecionado Picanha, valor: {strongonoff}")
            vetor_comida.append(18)
            repetir = input("Deseja outro pedido? ").upper()
            if repetir == "N":
                break
        case 4:
            print(f"Prato Selecionado Picanha, valor: {bife_acebolado}")
            vetor_comida.append(15)
            repetir = input("Deseja outro pedido? ").upper()
            if repetir == "N":
                break
        case 5:
            print(f"Prato Selecionado Picanha, valor: {pao_c_ovo}")
            vetor_comida.append(5)
            repetir = input("Deseja outro pedido? ").upper()
            if repetir == "N":
                break
        case _:
            print('Opção inválida. \nTente novamente... \n')


soma = sum(vetor_comida)

print(f"Valor {soma}")
