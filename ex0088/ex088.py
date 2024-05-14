# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep
lista = []
jogos = []
print('-' * 30)
print('    JOGA NA MEGA SENA    ')
print('-' * 30)
quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
total = 1
while total <= quantidade:
    cont = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            cont += 1
            if cont >= 6:
                break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print('-=' * 3, f' SORTEANDO {quantidade} JOGOS ', '-=' * 3)
for indice, naLista in enumerate(jogos):
    print(f'Jogo {indice+1}: {naLista}')
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)