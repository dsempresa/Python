# Crie um programa que leia dois valores e mostre um menu na tela.
# [ 1 ] SOMAR
# [ 2 ] MULTIPLICAR
# [ 3 ] MAIOR
# [ 4 ] NOVOS NÚMEROS
# [ 5 ] SAIR DO PROGRAMA
# Seu programa deverá realizar a operação solicitada em cada caso 
from time import sleep
num1 = float(input('Digite um número: '))
num2 = float(input('Digite um número: '))
print('O que você deseja fazer com esses dois valores?')
print('=-' * 25)
sleep(2)
print('''[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA''')
opcao = int(input('Digite sua opção:'))
while opcao == 1 or opcao == 2 or opcao == 3 or opcao == 4:
    if opcao != 4 :
        if opcao == 1:
            print('A soma entre {} + {} = {}'.format(num1,num2,num1+num2)) 
            print('=-' * 25)
            sleep(2)    
        if opcao == 2:
            print('O produto de {} x {} = {}'.format(num1,num2,num1*num2))
            print('=-' * 25)
            sleep(2)  
        if opcao == 3:
            if num1 > num2:
                print('O 1º número digitado -> {} é maior que o 2º número digitado -> {}'.format(num1,num2))
                print('=-' * 25)
                sleep(2)  
            elif num1 < num2:
                print('O 1º número digitado -> {} é menor do que o 2º número digitado -> {}'.format(num1,num2))
                print('=-' * 25)
                sleep(2)  
            else:
                print('Os dois números são iguais.')
                print('=-' * 25)
                sleep(2)  
        print('''[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA''')    
        opcao = int(input('Digite sua opção:'))
    if opcao == 4:            
        num1 = float(input('Digite um número: '))
        num2 = float(input('Digite um número: '))
        print('O que você deseja fazer com esses dois valores?')
        print('=-' * 25)
        sleep(2)
        print('''[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA''')
        opcao = int(input('Digite sua opção:'))
        print('=-' * 25)
if opcao == 5:
    print('Fim do programa!!!!')
else:
    print('Número inválido!!!!!!!')

    
     





