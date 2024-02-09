# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero ate vinte.
# Seu programa devera ler um numero pelo teclado(entre 0 e 20) e mostra-lo por extenso.

cont = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez',
        'onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito',
        'dezenove','vinte')
while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente. ', end='')

print(f'Voce digitou o numero {cont[num]}')