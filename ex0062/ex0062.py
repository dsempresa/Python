# Melhore o desafio 61,perguntando para o usuario se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos 

print('Gerador de PA:')
print('-='*20)
pn = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
total = 0
termo = pn
contador = 1
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print('{} -> '.format(pn), end='')
        pn += r
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos termos voce quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))

