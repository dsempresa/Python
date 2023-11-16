'''
Desenvolva um programa que pergunte a distancia de uma viagem em km.Calcule o preço da passagem,cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas.

'''

distancia = float(input('Qual a distância que precisaremos percorrer para chegar ao nosso destino? '))
if distancia <= 200:
    passagem = distancia * 0.50
    print('Sua passagem custará R${:.2f}'.format(passagem))
else:
    passagem = distancia * 0.45
    print('Sua passagem custará R${:.2f}'.format(passagem))