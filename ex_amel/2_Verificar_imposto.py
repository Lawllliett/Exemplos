'''Verificar Imposto
Crie um programa para determinar se uma pessoa deve ou não pagar impposto. COnsidere que pagam imposto 
pessoas cujo salário é maior que R$1.200,00'''


def ssalario():
    seusalario = float(input("Digitr seu salário: "))
    return seusalario


def calcularimposto(seusalario):
    if seusalario >= 1200:
        print(
            f'Seu salário é de R${seusalario}\nPortanto você deve pagar o imposto\n')
    else:
        print(
            f'Seu salário é de R${seusalario}\nLogo você não deve pagar o imposto\n')


seusalario = ssalario()
calcularimposto(seusalario)
