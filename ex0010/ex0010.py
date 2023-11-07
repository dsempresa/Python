'''Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e quantos dólares ela consegue comprar. considere US$1,00 = R$3,27'''

carteira = float(input('Quanto em R$ você tem na carteira nesse momento? '))
uss = 3.27

converter = carteira / uss
print('Com o valor de R${} que você tem na carteira, você conseguirá comprar US${}.'.format(carteira, converter))