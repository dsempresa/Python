'''Escreva um programa que pergunte a quantidade de km percorridos por um carro ealugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por km rodado'''

km = float(input('Quantos km você percorreu com o carro? '))
dias = int(input('Quantos dias você alugou o carro? '))
valorPorDia = dias * 60
valorPorKm = km * 0.15
valorApagar = valorPorDia + valorPorKm
print('Com essa quantidade de {}km e com {} dias de aluguel, o valor a pagar será de R${}.'.format(km, dias, valorApagar))