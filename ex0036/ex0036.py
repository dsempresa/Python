# Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal,sabendo que ela não pode exceder 30% do salario ou então o emprestimo será negado.

imovel = float(input('Qual valor do imóvel desejado? '))
anos = int(input('Em quantos anos pretende quitar o imóvel? '))
salario = float(input('Qual seu salario mensal? '))
parcelas = anos * 12
valorCasa = parcelas * ((30 * salario) / 100)
if valorCasa >= imovel:
    print('Esse empréstimo no valor de R${:.2f} será aprovado pelo banco, e será pago em {} parcelas fixas de R${:.2f} '.format(valorCasa, parcelas,((30 * salario) / 100)))
else:
    print('Emprestimo negado!')


