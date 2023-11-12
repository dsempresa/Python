'''
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados
EX:
Digite um número:1834
unidade:4
dezena:3
centena:8
milhar:1
'''

# num = str(input('Digite um número: '))
# num.split()
# unidade = num[3]
# dezena = num[2]
# centena = num[1]
# milhar = num[0]

# print('unidade {}\ndezena {}\ncentena {}\nmilhar {}'.format(unidade,dezena,centena,milhar))

# num = int(input('Digite um número: '))  '''usando string
# n = str(num)
# print('unidade {}\ndezena {}\ncentena {}\nmilhar {}'.format(n[3],n[2],n[1],n[0]))

num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('unidade {}\ndezena {}\ncentena {}\nmilhar {}'.format(u,d,c,m))




