# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 a 50.

inicio = 1
fim = 50
for c in range(inicio, fim):
    if c%2!=0:
        c+=1
        print(c)