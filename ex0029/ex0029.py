'''
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h,mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada km acima do limite.
'''

velocidade = float(input('Velocidade capturada pelo radar: '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Nessa velocidade de {:.2f}km/h você ultrapassou o limte de velocidade que é 80km/h.\nVocê será multado em R${:.2f}!'.format(velocidade, multa))
else:
    print('Dirija com cuidado!')