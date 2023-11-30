# # for c in range(1,10):
# #     print('Oi')
# # print('Fim')
# s = 0
# for c in range(0,3):
#     n = int(input('Digite um número: '))
#     s += n
# print('O somatório dos números é {}'.format(s))


# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificios,indo de 10 até 0,com uma pausa de 1 segundos entre eles.
from time import sleep
from emoji import emojize
print('Contagem regressiva...')
print('-='* 5)
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(emojize('🎆🎆🎆🎆🎆🎆🎆🎆🎆🎆'))