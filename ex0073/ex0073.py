# lanche  = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita')
# for cont in range(0, len(lanche)):
#     print(f'Eu vou comer {lanche[cont]} na posição {cont}')


# for pos, comida in enumerate(lanche):
#     print(f'Eu vou comer {comida} na posição {pos}')
# print('Comi pra caramba!!!!')

# Crie uma tupla preenchida com os 20 primeiros colocados da tabela do brasileirão,na ordem de colocação. Depois mostre:
# A- Apenas os 5 primeiros colocados
# B- Os ultimos 4 colocados
# C- Uma lista com times em ordem alfabética
# D- Em que posição na tabela está o time do Fortaleza.

listaDeTimes = ('Palmeiras', 'Gremio', 'Atletico mg', 'Flamengo', 'Botafogo',
                'Bragantino', 'Fluminense', 'Atletico PR', 'Internacional',
                'Fortaleza', 'Sao paulo', 'Cuiaba', 'Corinthians', 'Cruzeiro',
                'Vasco', 'Bahia', 'Santos', 'Goias', 'Coritiba', 'America')
# print('lista de times', {listaDeTimes})
for time in listaDeTimes:
    print(time)
print('-=' * 10)
print(f'Os 5 primeiros são {listaDeTimes[0:5]}')
print('-=' * 10)
print(f'Os 4 ultimos são {listaDeTimes[-4:]}')
print('-=' * 10)
print(f'Times em ordem alfabetica: {sorted(listaDeTimes)}')
print('-=' * 10)
print(f'O Fortaleza está na {listaDeTimes.index("Fortaleza")+1}ª posição')