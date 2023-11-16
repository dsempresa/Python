'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.

Para salários superiores a R$1250,00,calcule um aumento de 10%.

Para salários inferiores ou iguais, o aumento será de 15%
'''

salario = float(input('Qual seu salário atual? '))
if salario > 1250:
    aumento1 = ((10 * salario) / 100) + salario
    print('Parabens pelo seu aumento.\nAntes vc recebia R${:.2f} de salário e agora receberá R${:.2f} com seu aumento de 10%'.format(salario, aumento1))
else:
    aumento2 = ((15 * salario) / 100) + salario
    print('Parabens pelo seu aumento.\nAntes vc recebia R${:.2f} de salário e agora receberá R${:.2f} com seu aumento de 15%'.format(salario, aumento2))