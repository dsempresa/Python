'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo,calcule e mostre o comprimento da hipotenusa. '''

# catetoOposto = float(input('Digite o comprimento do cateto oposto do triangulo: '))
# catetoAdjacente = float(input('Digite o comprimento do cateto adjacente do triângulo: '))
# hipotenusa = ((catetoOposto ** 2) + (catetoAdjacente ** 2)) ** (1 / 2)
# print(hipotenusa)

import math
catetoOposto = float(input('Digite o comprimento do cateto oposto do triangulo: '))
catetoAdjacente = float(input('Digite o comprimento do cateto adjacente do triângulo: '))
hi = math.hypot(catetoOposto, catetoAdjacente)
print('A hipotenusa vai medir {:.2f}'.format(hi))
