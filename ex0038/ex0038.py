# Escreva um programa que leia dois numeros inteiros e compare-os mostrando na tela uma mensagem:

# - O primeiro valor é maior
# - O segundo valor é maior
# - N existe valor maior, os dois são iguais

num1 = int(input('Digite o 1° valor: '))
num2 = int(input('Digite o 2° valor: '))
if num1 > num2:
    print('O 1° valor digitado é maior do que o 2°!')
elif num2 > num1:
    print('O 2° valor digitado é maior do que o 1°!')
else:
    print('Os dois valores são iguais!')