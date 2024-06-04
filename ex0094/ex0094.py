# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média
cadastro = {}
pessoas = [cadastro]
while True:
    cadastro['nome'] = str(input('Nome: '))
    while True:
        cadastro['sexo'] = str(input('Sexo: [M/F] '))
        if cadastro['sexo'] not in 'MmFf':
            print('ERRO! Por favor, digite apenas M ou F.')
        else:
            cadastro['idade'] = int(input('Idade: '))
            break 
        
    while True:
        cadastro['r'] = (str(input('Quer continuar? [S/N]')))
        if cadastro['r']not in 'SsNn':
            print('ERRO! Digite apenas S ou N.')
        if cadastro['r'].upper() == 'S':
            break
        if cadastro['r'].upper() == 'N':
            break
    break

del cadastro['r']
print(pessoas)
        

        

       