# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final,mostre:
# A- Quantas vezes apareceu o numero 9.
# B- Em que posição foi digitado o primeiro valor 3.
# C- Quais foram os numeros pares.

n = (int(input('Digite um número: ')),
    int(input('Digite um número: ')),
    int(input('Digite um número: ')),
    int(input('Digite um número: ')))
print(f'Você digitou os valores {n}')
print(f'O valor 9 apareceu {n.count(9)} vezes.')
if 3 in n:
    print(f'O valor 3 apareceu na {n.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print('Os valores pares digitados foram ', end='')
for numero in n:
    if numero % 2 == 0:
        print(numero, end=' ')