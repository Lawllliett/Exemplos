'''Cálculo de desconto progressivo
Crie um programa que peça o valor de um produto e a quantidade comprada. Aplique um desconto de 5% para 3 
unidades ou mais e 10 % para 5 unidades ou mais'''


def produto():
    valor = int(input("Informe o valor do produto: R$ "))
    quantidade = int(input("Informe a quantidade comprada: "))
    return valor, quantidade


def calcular_desconto(valor, quantidade):
    if quantidade >= 5:
        desconto = 0.10
    elif quantidade >= 3:
        desconto = 0.05
    else:
        desconto = 0.0

    valor_total = valor * quantidade
    valor_com_desconto = valor_total * (1 - desconto)

    print(f"\nValor total sem desconto: R$ {valor_total:.2f}")
    print(f"Desconto aplicado: {desconto * 100:.0f}%")
    print(f"Valor final com desconto: R$ {valor_com_desconto:.2f}")


preco, qtd = produto()
calcular_desconto(preco, qtd)
