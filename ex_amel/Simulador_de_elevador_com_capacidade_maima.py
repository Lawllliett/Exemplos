def elevador():
    while True:
        qpessoas = int(
            input("Informe a quantidade de pessoas no elevador (máx. 4): "))
        if qpessoas > 4:
            print("Número máximo de pessoas é 4. Tente novamente.\n")
            continue
        peso_total = 0
        for n in range(qpessoas):
            peso = int(input("Qual o peso dessa pessoa? "))
            peso_total += peso
        return peso_total


def peso_elevador(peso_total):
    if peso_total > 300:
        print("Peso máximo de 300 kg excedido")
    else:
        print("Peso máximo não excedido")


total = elevador()
peso_elevador(total)
