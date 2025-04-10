'''Simulador de pedágio dinâmico
Crie um programa que peça o tipo de veículi (carro, caminhão, moto) e calcule o valor do pedágio com base nesses
fatores'''


def veiculo():
    while True:
        print("Qual o tipo do seu veículo?\n 1 - Carro\n 2 - Caminhão\n 3 - Moto")
        escolha = int(input("Digite um número correspondente: "))

        if escolha == 1:
            return "carro"
        elif escolha == 2:
            return "caminhao"
        elif escolha == 3:
            return "moto"
        else:
            print("Opção inválida. Tente novamente.\n")


def calcular_pedagio(tipo):
    if tipo == "carro":
        valor = 10.0
    elif tipo == "caminhao":
        valor = 20.0
    elif tipo == "moto":
        valor = 5.0
    else:
        valor = 0.0

    print(f"Veículo: {tipo}")
    print(f"Valor do pedágio: R$ {valor:.2f}")


tipo_veiculo = veiculo()
calcular_pedagio(tipo_veiculo)
