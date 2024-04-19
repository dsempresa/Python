# Crie um programa que vai ler varios numeros e colocar em uma lista.

# Depois disso,crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados,respectivamente.

# Ao final, mostre o conteudo das tres listas geradas.
numeros = []
pares = []
impares = []
while True:
    n = int(input('Digite um valor: '))
    numeros.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print(f'A lista completa de numeros é {numeros}.')
print(f'A lista de pares é {pares}.')
print(f'A lista de ímpares é {impares}.')
