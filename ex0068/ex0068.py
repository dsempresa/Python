# #Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador perder,mostrando o total de vitorias consecultivas que ele conquistou no final do jogo.
from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!!!!')
            v += 1
        else:
            print('Você PERDEU!!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!!!!')
            v += 1
        else:
            print('Você PERDEU!!!!')
            break
    print('Vamos jogar novamente...')
print(f'Game over! Você venceu {v} vezes')





