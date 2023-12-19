# Refaça o desafio 51,lendo o primeiro termo e a razão de uma PA,mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('Gerador de PA:')
print('-='*20)
n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
# termo = n
contador = 1
while contador <= 10:
    print('{} -> '.format(n), end='')
    n += r
    contador += 1
print('FIM!!!!!!!!!')