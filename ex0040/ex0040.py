# Crie um programa que leia duas notas de um aluno e calcule sua média,mostrando uma mensagem no final,de acordo com sua média atingida:

# -Média abaixo de 5.0:
# REPROVADO
# -Média entre 5.0 e 6.9:
# RECUPERAÇÃO
# -Média 7.0 ou superior:
# APROVADO

nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite a 2ª nota: '))
media = (nota1 + nota2) / 2
if media >= 7.0:
    print('Parabens, com uma média de {}, você está \033[1;30;42m APROVADO \033[m!!!!'.format(media))
elif media >= 5.0 and media < 7:
    print('Atenção,com uma média de {}, você está de \033[1;37;43m RECUPERAÇÃO \033[m!!!!'.format(media))
else:
    print('Com uma média de {},você está \033[1;30;41m REPROVADO \033[m!!!!!'.format(media))