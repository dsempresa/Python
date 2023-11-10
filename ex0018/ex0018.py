'''Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.'''
import math
angulo = float(input('Digite o angulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O seno é {:.2f}\nO cosseno é {:.2f}\nA tangente é {:.2f}'.format(seno, cosseno, tangente))





