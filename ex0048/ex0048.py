# Faça um programa que calcule a soma entre todos os números ímpares que são multiplos de tres e que se encontram no intervalo de 1 até 500.

inicio = 1
fim = 501
pulo = 2
soma = 0
contador = 0
for c in range(inicio, fim, pulo):
    if c % 3 == 0:
        contador = contador + 1
        soma = soma + c
print('A soma de todos os {} valores solicitados é {}'.format(contador,soma))
