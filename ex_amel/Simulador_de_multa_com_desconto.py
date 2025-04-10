'''Simulador de Multa com descontos
Crie um programa e peça a velocidade de um carro e informe se ele será multado. O valor de multa é de R$ 5,00
por km acima do limite de 80km/h, mas se a velocidade estiver entre 81 e 85km/h, efereça um desconto de 50%'''


def VelCarro():
    velocidade = int(input("Qual foi a velocidade do carro? (Em km/h) "))
    return velocidade


def CalcularMulta(velocidade):
    if velocidade > 80:
        km_acima = velocidade - 80
        multa = km_acima * 5

        if 81 <= velocidade <= 85:
            multa *= 0.5

        print(f"Você foi multado! Valor da multa: R$ {multa:.2f}")
    else:
        print("Velocidade dentro do limite. Sem multa.")


vel = VelCarro()
CalcularMulta(vel)
