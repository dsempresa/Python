# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# ex:
# 5! = 5x4x3x2x1=120
# from math import factorial
# num = int(input('Digite um número: '))
# f = factorial(num)
# print('O factorial de {} é {}'.format(num,f))

num = int(input('Digite um número: '))
contador = num
f = 1
print('Calculando {}! = '.format(num), end='')
while contador > 0:
    print('{}'.format(contador), end='')
    print(' x ' if contador > 1 else ' = ', end='')
    f *= contador
    contador -= 1
print('{}'.format(f))

