'''Cálculo de preço com parcelamento
Crie um programa que peça  valor de um produto e a quantidade de parcelas (até 12). O programa deve calcular o 
valor de cada parcela, aplicando juros de 2% ao mês para compras parceladas acima de 6x. '''


def produto():
    produto = str(input("Informe o nome do produto: "))
    while True:
        quantidadep = int(input("Qual a quantidade de parcelas? "))
        if quantidadep <= 12:
            break
        print("A quantidade de parcelas é no máximo de 12 vezes! Informe um valor menor que isso\n")
    return produto, quantidadep


def calcparcelas(produto, quantidadep):
    valor = float(input("Informe o valor do produto: R$ "))
    if quantidadep > 6:
        juros = 0.02 * quantidadep
        valor_total = valor * (1 + juros)
    else:
        valor_total = valor

    parcela = valor_total / quantidadep

    print(f"\nProduto: {produto}")
    print(f"Valor total com juros: R$ {valor_total:.2f}")
    print(f"{quantidadep}x de R$ {parcela:.2f}")


prod, parcelas = produto()
calcparcelas(prod, parcelas)
