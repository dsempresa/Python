# Escreva um programa que leia um número inteiro qualquer e peça para o usuario escolher qual será a base da conversão:

# -1 para binário
# -2 para octal
# -3 para hexadecimal

num = int(input('Digite um número inteiro: '))
print('Escolha uma base pra conversão:\n[ 1 ] converter para BINÁRIO\n[ 2 ] converter para OCTAL\n[ 3 ] converter para HEXADECIMAL')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido pra BINARIO é igual a {}'.format(num, bin(num)))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)))
else:
    print('Opção inválida. Tente novamente!')