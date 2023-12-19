# Crie um programa que leia varios numeros inteiros pelo teclado. O programa so vai parar quando o usuario digitar o valor 999,que é a condição de parada. No final mostre quantos numeros foram digitados e qual foi a soma entre eles(desconsiderando flag).

n = soma = contador = 0
while True:
    n = int(input('Digite um numero(digite 999 para parar): '))
    if n == 999:
        break
    contador += 1
    soma = soma + n
print(f'Foram somados {contador} números, e a soma entre eles é {soma}')

