#Crie um programa que simule o funcionamento de um caixa eletronico. No inicio,pergunte ao usuario qual será o valor a ser sacado(numero inteiro) e o programa vai informar quantas cedulas de cada valor serão entregues.
#OBS: CONSIDERE QUE O CAIXA POSSUI CEDULAS DE R$50,00 , R$20,00 , R$10,00 , R$1,00.

print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
cedula = 50
totalDeCedula = 0
while True:
    if total >= cedula:
        total -= cedula
        totalDeCedula += 1
    else:
        if totalDeCedula > 0:
            print(f'Total de  {totalDeCedula} cedulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalDeCedula = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
