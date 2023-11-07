'''Faça um programa que leia a altura e a largura de uma parede em metros,calcule a sua área e a quantidade de tinta parapintá-la,sabendo que cada litro de tinta,pinta uma área de 2m².'''

altura = float(input('Qual a altura dessa parede? '))
largura = float(input('Qual a largura dessa parede? '))
area = altura * largura
tinta = area / 2

print('Com uma area de {}m²,iremos precisar de {} litros de tinta pra realizar a pintura da parede.'.format(area, tinta))