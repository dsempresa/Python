# A confederação Nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria,de acordo com a idade:

# -Até 9 anos: MIRIM
# -Até 14 anos: INFANTIL
# -Até 19 anos: JUNIOR
# -Até 20 anos: SÊNIOR
# -Acima: MASTER
import datetime
anoNasc = int(input('Ano de nascimento? '))
idade = datetime.date.today().year - anoNasc
if idade <= 9:
    print('Categoria Mirim')
elif idade > 9 and idade <= 14:
    print('Categoria Infantil')
elif idade > 14 and idade <= 19:
    print('Categoria Junior')
elif idade > 19 and idade <= 20:
    print('Categoria Senior')
else:
    print('Categoria Master')

