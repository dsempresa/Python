'''
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com nome "SANTO".
'''

# cidade = str(input('Qual cidade você nasceu? '))

# print(len(cidade.split()))
# print(cidade.count('SANTO',0))

cidade = str(input('Qual cidade você nasceu? ')).strip().upper()
print(cidade[:5] == 'SANTO')
