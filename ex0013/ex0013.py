'''Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.'''

salarioAtual = float(input('Qual valor do seu salário? '))
aumento = (15 * salarioAtual) / 100
novoSalario = salarioAtual + aumento

print('Seu salário hoje está em R${} mas com aumento de 15% você irá receber um novo salário de R${}.'.format(salarioAtual, novoSalario))