'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
*Nome com todas as letras maiúscular
*O nome com todas as letras minúsculas
*Quantas letras ao todo(sem considerar os espaços)
*Quantas letras tem o primeiro nome
'''

nome = str(input('Digite seu nome completo: '))
print(nome.upper())
print(nome.lower())
print(len(nome.replace(' ','').strip()))
dividido = nome.split()
print(len(dividido[0]))



