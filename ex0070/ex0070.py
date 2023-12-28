#Crie um programa que leia o nome e o preço de varios produtos. O programa deverá perguntar se o usuario vai continuar. No final mostre:
#QUAL O TOTAL GASTO NA COMPRA.
#QUANTOS PRODUTOS CUSTAM MAIS DE R$1000,00
#QUAL O NOME DO PRODUTO MAIS BARATO
totGasto = totMil = menor = contador = 0
barato = ''
while True:
    produto = str(input('Qual produto você comprou? '))
    preco = float(input(f'Qual preço do {produto}?'))
    contador += 1
    totGasto += preco
    if preco > 1000:
        totMil += 1
    if contador == 1 or preco < menor:
        menor = preco
        barato = produto
    contCompra = ' '
    while contCompra not in 'SN':
        contCompra = str(input('Vai continuar comprando aqui? ')).strip().upper()[0]    
    if contCompra == 'N':
        break
print('Acabou')
print(f'voce gastou um total de R${totGasto:.2f}')
print(f'Temos {totMil} prdutos custando mais de R$1000,00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')


