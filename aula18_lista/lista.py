# lanche = ['bolo', 'pizza', 'suco', 'pudim', 'picole']
# lanche.append('cooks')
# lanche.insert(0, 'cachorro quente')
# print(lanche)

# num = [2, 5, 9, 1]
# num[2] = 3
# num.append(7)
# num.sort(reverse=True)
# num.insert(2, 2)
# num.remove(2)
# print(num)
# print(f'Essa lista tem {len(num)} elementos.')

valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
