# Faça um programa que leia o ano de nascimento de um jovem e informe,de acordo com sua idade:

# - Se ele ainda vai se alistar ao serviço militar
# - Se é a hora de se alistar
# - Se ja passou do tempo do alistamento

# Seu programa tambem deverá mostrar o tempo que falta ou que ja passou do prazo
from datetime import date
nome = str(input('Digite seu nome: '))
anoNascimento = int(input('Digite o ano do seu nascimento: '))
idade = date.today().year - anoNascimento
if idade == 18:
    print('{}, com idade de {} anos já está na hora de você se alistar!'.format(nome, idade))
elif idade > 18:
    print('{}, com idade de {} anos, já passou da hora certa de se alistar!'.format(nome, idade))
else:
    print('{}, com apenas {} anos você ainda não pode se alistar!'.format(nome, idade))


