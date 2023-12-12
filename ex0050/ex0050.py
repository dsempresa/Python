# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar,desconsidere-o.
soma = 0
contador = 0
for c in range(1, 7):
    num = int(input('Digite o {}° número: '.format(c)))
    if num % 2 == 0:
        soma += num
        contador += 1
print('A soma de todos os {} números pares é {}'.format(contador,soma))

