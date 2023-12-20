# Faça um programa que mostre a tabuada de varios numeros,um de cada vez,para cada valor digitado pelo usuario. O programa será interrompido quando o numero solicitado for negativo.
# print('='*20,'PROGRAMA TABUADA','='*20)
# num = int(input('Quer vê a tabuada de qual valor? '))
# print('='*20,'PROGRAMA TABUADA','='*20)
# num = int(input('Quer vê a tabuada de qual valor? '))
# contador = 0
# while contador < 10:
#     while True:
#         # while contador < 10:
        
#         tabuada = print(f'{num} x {contador} = {num*contador}')
#         contador += 1
#         if contador == 10:
#             while True:
#                 print('='*20,'PROGRAMA TABUADA','='*20)
#                 num = int(input('Quer vê a tabuada de qual valor? '))
#     # if num < 0:
#     #     break
   
    
    
#         # if contador == 10:
#         #     break
# print('Programa de tabuada encerrada. Volte sempre!!!!!!')
while True: 
    
    num = int(input('Quer le a tabuada de qual valor?'))
    if num < 0:
        break
    print('='*20,'PROGRAMA TABUADA','='*20)
    for c in range(1,11):
        print(f'{num} x {c} = {num*c}')
    print('='*20,'PROGRAMA TABUADA','='*20)
print('Programa de tabuada encerrada!')
   
    


    