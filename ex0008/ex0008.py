'''Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.'''

metro = float(input('Quantos metros mede essa parede? '))
centi = metro * 100
mili = centi * 10
print('Já que essa parede tem {}m, isso significa que ela tem {}cm e {}mm'.format(metro, centi, mili))