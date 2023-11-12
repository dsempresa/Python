'''
Faça um programa que leia um nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.
EX:Ana Maria de Sousa
primeiro = Ana
ultimo = Souza
'''

seuNome = str(input('Digite seu nome completo: '))
nome = seuNome.split()
print('O seu primeiro nome é {}'.format(nome[0]))
print('O seu ultimo nome é {}'.format(nome[len(nome) - 1]))