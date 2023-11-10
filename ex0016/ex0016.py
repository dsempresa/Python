'''Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.'''
'''Exemplo: digite um número:6.127
O número 6.127 tem a parte inteira 6.'''
# import math
# num = float(input('Digite um valor: '))
# print('{}'.format(math.trunc(num)))

num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))