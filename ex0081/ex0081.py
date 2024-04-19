# Crie um programa que vai ler varios numeros e colocar em uma lista.

# Depois disso,mostre:
# A) Quantos numeros foram digitados.
# b) A lista de valores ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

numeros = []
while True:
    n = int(input('Digite um valor: '))
    numeros.append(n)
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print(f'Você digitou {len(numeros)} elementos.')
numeros.sort(reverse=True)
print(f'Você digitou os valores em ordem decrescente são {numeros}.')
if 5 in numeros:
    print(f'O valor 5 faz parte da lista.')
else:
    print('O valor 5 não faz parte da lista.')
