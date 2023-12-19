# Crie um programa que leia varios numeros inteiros pelo teclado. O programa só vai parar quando o usuário digitar 999,que é a condição de parada. No final, mostree quantos números foram digitados e qual foi a soma entre eles(desconsiderando flag).

# num = 0
# contador = 0
# soma = 0
num = contador = soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma += num
    contador += 1
    num = int(input('Digite um número [999 para parar]: '))
print('Voce digitpou {} numeros e a soma entre eles foi {}!'.format(contador, soma))