#  Aprimore o desafio anterior, mostrando no final:                                                    A) A A) A soma de todos os valores pares digitados.                                                                                                  B) A soma dos valores da terceira coluna.                                                                                                      C) O maior valor da segunda linha.

matriz = [[0,0,0],[0,0,0],[0,0,0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
print('-=' * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()

