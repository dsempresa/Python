#Crie um programa que leia a idade e o sexo de varias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final mostre:
#QUANTAS PESSOAS TEM MAIS DE 18 ANOS
#QUANTOS HOMENS FORAM CADASTRADOS
#QUANTAS MULHERES TEM MAIS DE 20 ANOS.

print('-'*30)
print('CADASTRE UMA PESSOA')
print('-'*30)
tot18 = totH = totM20 = 0
while True:
    idade = int(input('idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F ]')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade <= 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?  [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Pessoas com mais de 18 anos: {tot18} ')
print(f'Ao todo temos {totH} homens cadastrados. ')
print(f'Temos {totM20} mulheres com menos de 20 anos de idade. ')


