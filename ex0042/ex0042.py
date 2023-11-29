# Reforça o desafio 035 dos triangulos,acrescentando o recurso de mostrar que tipo de triângulo será formado:

# -Equilatero: todos os lados iguais
# -Isosceles: dois lados iguais
# -Escaleno: todos os lados são diferentes

reta1 = float(input('Digite a 1ª reta: '))
reta2 = float(input('Digite a 2ª reta: '))
reta3 = float(input('Digite a 3ª reta: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Os seguimentos acima formam um triangulo ', end='')
    if reta1 == reta2 == reta3:
        print('EQUILATERO!')
    if reta1 != reta2 != reta3 != reta1:
        print('ESCALENO!')
    else:
        print('ISORCELES!')
else:
    print('Os seguimentos acima não formam um triangulo ')