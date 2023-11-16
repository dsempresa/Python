'''
Faça um programa que leia tres numeros e diga qual o menor e qual o maior
'''

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))
#Verificando menor valor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2 
if n3 < n1 and n3 < n2:
    menor = n3
#verificando maior valor
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
