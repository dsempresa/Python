# Crie um programa onde o usuario possa digitar varios valores numericos e cadastre-os em uma lista. Caso o numero ja exista la dentro,ele não sera adicionado.No final,serão exibidos todos os valores unicos digitados, em ordem crescente.

variosValores = []
while True:
    n = int(input('Digite um valor: '))
    if n not in variosValores:
        variosValores.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')

    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break

print('-=' *40)
variosValores.sort()
print(f'Voce digitou os valores {variosValores}.')
