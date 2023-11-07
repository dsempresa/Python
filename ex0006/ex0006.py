'''Crie um algoritmo que leia um número e mostre o seu dobro,triplo e raiz quadrada.'''

num = int(input('Digite um número: '))
dobro = num * 2
triplo = num * 3
raiz = num ** (1/2)
print('O dobro de {} é {} \nO triplo de {} é {} \nA raiz quadrada de {} é {:.2f}'.format(num, dobro, num, triplo, num, raiz))