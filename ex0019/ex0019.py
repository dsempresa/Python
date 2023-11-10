'''Um professor quer sortear um dos seus quatro alunos pra apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.'''
import random
aluno1 = input('Nome do 1° aluno: ')
aluno2 = input('Nome do 2° aluno: ')
aluno3 = input('Nome do 3° aluno: ')
aluno4 = input('Nome do 4° aluno: ')
lista = [aluno1,aluno2,aluno3,aluno4]
sorteado = random.choice(lista)
print('O aluno sorteado foi {}'.format(sorteado))
