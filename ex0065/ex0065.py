# Crie um programa que leia varios numeros inteiros pelo teclado. No final da execução,mostre a media entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuario se ele quer ou não continuar a digitar valores.

resp = 'S'
soma = quantidade = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    soma += num
    quantidade += 1
    if quantidade == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
media = soma / quantidade
print('Voce digitou {} numeros e a media foi {}'.format(quantidade,media))
print('O maior valor foi {} e o menor valor foi {}'.format(maior,menor))
