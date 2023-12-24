#Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador perder,mostrando o total de vitorias consecultivas que ele conquistou no final do jogo.
from random import randint
contador1 = 0
contador2 = 0
print('=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR')

while True:
    print('=-'*20)
    jogador = int(input('Diga um valor: '))
    parOuImpar = str(input('Par ou Ímpar? [P/I] '))
    computador = randint(0,10)
    resultado = jogador + computador
    print('-'*30)
    if resultado % 2 == 0:
        print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {resultado}.')  
        if parOuImpar != 'Pp':  
            print('DEU PAR')
            print('Você venceu!')
            print('Vamos jogar novamente...')
            print('-'*30)
            contador1 += 1
    else:
        break 
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {resultado}.')
    print('DEU ÍMPAR')
    print('Você PERDEU!!!!!')
    if resultado % 2 != 0:
        print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {resultado}')
        if parOuImpar != 'Ii':
            print('DEU ÍMPAR')
            print('Você venceu!')
            print('Vamos jogar novamente...')
            contador2 += 1
    else:
        break   
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {resultado}.')
    print('DEU PAR')
    print('Você PERDEU!!!!!')
            
    # else:
    #     
    # else:
    # print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {resultado}.')
    # print('DEU PAR')
    # print('Você PERDEU!!!!!')
    # break
    
        
        # if jogador + computador % 2 != 0 and parOuImpar == 'Pp':
    # else:
    #     print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {resultado}, deu PAR')
    #     break
    # if jogador + computador % 2 == 0 and parOuImpar == 'Ii':
    #     break
        # print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {jogador + computador}, deu ÍMPAR')
        
    # if jogador + computador % 2 != 0 and parOuImpar == 'Pp':
    #     break
        # print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {jogador + computador}, deu PAR')
        

print('=-'*20)
print(f'GAME OVER!! Você venceu {contador1 + contador2} vezes')

    




