'''Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.'''

num = int(input('Digite um número: '))
ant = num - 1
suc = num + 1

print('O numero {} tem como antecessor o número {} e como sucessor o número {}'.format(num, ant, suc))