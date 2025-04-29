'''Simulador de estoque
Peça o nome de um produto e quantidades de entrada e saída e mostre o saldo final.
'''


def mostrar_menu():
    print("\nOpções")
    print("1. Adicionar novo produto")
    print("2. Mostrar estoque")
    print("3. Sair")


def lista_produtos(estoque):
    produto = input("Nome do produto: ")
    qinicial = int(input(f'Digite a quantidade inicial de {produto}\n'))
    qfinal = int(input(f'Digite a quantidade de saída de {produto}\n'))
    saldo_final = qinicial - qfinal
    estoque.append({"produto": produto, "saldo": saldo_final})
    print(f"{produto} adicionado com saldo final de {saldo_final} unidades.")
    return saldo_final


def mestoque(estoque):
    print(f'Estoque:\n')
    for produto in estoque:
        print(f"{produto['produto']}: {produto['saldo']} unidades")


def main():
    estoque = []
    while True:
        mostrar_menu()
        opcao = int(input("Digite uma opção: "))
        if opcao == 1:
            lista_produtos(estoque)
        elif opcao == 2:
            mestoque(estoque)
        elif opcao == 3:
            break
        else:
            print("Digite uma opção válida: ")


main()
