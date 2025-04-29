'''Peso Ideal
Tendo como dados de entrada a altura de uma pessoa, construa um algorritmo que calcule seu peso ideal, usando a 
seguinte fórmula: 
(72.7 * altura) - 58
'''


def inserir_peso():
    altura = float(input("Coloque sua altura: "))
    return altura


def calculr_peso(altura):
    altura = altura
    peso_ideal = (72.7 * altura) - 58
    return peso_ideal


def resposta(peso_ideal, altura):
    print(f'Seu peso ideal com {altura} de altura é: {peso_ideal}')


altura = inserir_peso()
peso_ideal = calculr_peso(altura)
resposta(peso_ideal, altura)
