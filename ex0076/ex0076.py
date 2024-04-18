# Crie um programa que tenha uma tupla unica com nomes de produtos e seus respectivos preços,na sequencia.
# No final,mostre uma listagem de preços,organizando os dados em forma tabular.
print('-'*50)
print(' '*12, 'LISTAGEM DE PREÇOS', ' '*12)
print('-'*50)
listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.9,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'canetas', 22.30,
            'Livro', 34.90)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>6.2f}')

