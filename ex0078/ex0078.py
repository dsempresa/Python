# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e menor valor digitado e as suas respectivas posições na lista.

valores = []
maior = 0
menor = 0
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))
    if cont == 0:
        maior = menor = valores[cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]
print(f'Os valores digitados foram {valores}.') 
print('-=' *30)   
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for indice, valor in enumerate(valores):
    if valor == maior:
        print(f'{indice}... ' , end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for indice, valor in enumerate(valores):
    if valor == menor:
        print(f'{indice}... ' , end='')
print()


