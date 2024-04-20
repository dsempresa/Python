# dados = []
# dados.append('Pedro')
# dados.append(25)
# print(dados[0])
# print(dados[1])

# pessoas = []
# pessoas.append(dados[:])
# print(pessoas)

# pessoas = [['Pedro',25],['Maria', 19],['João',32]]

# print(pessoas[0][0])
# print(pessoas[:2])

# teste = []
# teste.append('Gustavo')
# teste.append(40)
# galera = []
# galera.append(teste[:])
# teste[0] = 'Maria'
# teste[1] = 22
# galera.append(teste[:])
# print(galera)

# galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
# for p in galera:
#     print(f'{p[0]} tem {p[1]} anos de idade.')

galera = []
dado = []
totmai = totmen = 0
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1

print(f'Temos {totmai} maiores e {totmai} menores de idade.')