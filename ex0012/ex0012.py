'''Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.'''

preco = float(input('Qual valor desse produto? '))
desconto = (5 * preco) / 100
valorFinal = preco - desconto
print('O valor do produto custa R${},mas com desconto de {}%, ele cairá pra R${}.'.format(preco, desconto, valorFinal))