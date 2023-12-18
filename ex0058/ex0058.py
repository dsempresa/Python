# Melhore o jogo do desafio 28 onde o pc vai pensar em um numero entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,mostrando no final quantos palpites foram necessários para vencer.

# import time
# import random 
# contador = 1
# numero = int(input('qual número o computador está pensando? '))
# time.sleep(2)
# pc = int(random.randint(0, 10))
# print('número escolhido pelo computador foi...{}'.format(pc))
# while numero != pc:    
#     print('Vc errou!\nTente outra vez!')
#     numero = int(input('qual número o computador está pensando? '))
#     time.sleep(2)
#     pc = int(random.randint(0, 10))
#     print('número escolhido pelo computador foi...{}'.format(pc))
#     contador += 1
# else:
#     print('Parabens você acertou em {} tentativas'.format(contador))


from random import randint
computador = randint (0,10)
print('Sou seu computador e acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite?'))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas'.format(palpites))
    