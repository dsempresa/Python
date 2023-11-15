'''
Escreva um programa que faça o computador pensar em um número inteiro de 0 a 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''
import time
import random 
numero = int(input('qual número o computador está pensando? '))
time.sleep(2)
pc = int(random.randint(0, 5))
print('número escolhido pelo computador foi...{}'.format(pc))
if numero == pc:
    print('Parabens você acertou')
else:
    print('Vc errou!\nTente outra vez!')

