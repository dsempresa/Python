# Crie um programa que vai gerar 5 numeros aleatorios e colocar em uma tupla.
# Depois disso,mostre a listagem de numeros gerados e tambem indique o menor e o maior valor que estão na tupla.

from random import randint
numero = (randint(1, 100), randint(1, 100),randint(1, 100), randint(1, 100),
           randint(1, 100) )
print('Eu sorteei os números: ', end='')
for n in numero:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(numero)}')
print(f'O menor valor sorteado foi {min(numero)}')
