# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,calcule seu IMC e mostre seu status,de acordo com a tabela abaixo:

# -Abaixo de  18.5:Abaixo do Peso
# -Entre 18.5 e 25:Peso ideal
# -25 até 30:Sobrepeso
# -30 até 40:Obesidade
# -Acima de 40:Obesidade mórbida

altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / (altura * altura)

if imc < 18.5:
    print('Seu IMC é {},Você está abaixo do peso ideal.'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Seu IMC é {},Você está com peso ideal.'.format(imc))
elif imc >= 25 and imc < 30:
    print('Seu IMC é {},Você está sobrepeso.'.format(imc))
elif imc >= 30 and imc <= 40:
    print('Seu IMC é {},Você está obeso.'.format(imc))
else:
    print('Seu IMC é {},Você está em obesidade mórbida.'.format(imc))