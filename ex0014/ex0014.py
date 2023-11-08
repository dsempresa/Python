'''Escreva um programa que converta uma temperatura digitada em °C e converta para °F.'''

tem = float(input('Qual a temperatura atual? '))
temFah = (tem * 9/5) + 32
print('Temperatura atual de °{}C convertida em fahrenheit ficará °{}F.'.format(tem, temFah))