# Faça um programa que leia o sexo de uma pessoa e só aceite os valores 'M' ou 'F'. Caso esteja errado,peça a digitação novamente até ter um valor correto.

print('========= Cadastro de funcionário ========')
nome = str(input('Nome: '))
sexo = str(input('Sexo: ')).upper()
while sexo not in 'MmFf':
    nome = str(input('Nome: '))
    sexo = str(input('Sexo: '))
print('Seu nome é {} e seu sexo é {}'.format(nome,sexo).upper())