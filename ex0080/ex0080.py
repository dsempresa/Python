# Crie um programa onde o usuario possa digitar cinco valores numericos e cadastre-os em uma lista,ja na posição correta de inserção(sem usar o sort()). No final,mostre a lista ordenada na tela.

lista = []
for contador in range(0, 5):
    n = int(input('Digite um valor: '))
    if contador == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1

print('-=' *30)
print(f'Os valores digitador em ordem foram {lista}.')

