# Elabore um programa que calcule o valor a ser pago por um produto,considerando o seu preço normal e condição de pagamento:

# -A vista dinheiro/cheque:10% de desconto
# -A vista no cartão:5% de desconto
# -Em ate 2x no cartão:preço normal
# -Em 3x ou mais no cartão:20% de juros

precoProduto = float(input('Digite o valor do produto: R$'))
formaPagamento = int(input('Digite a forma de pagamento:\n[ 1 ] Dinheiro ou Cheque\n[ 2 ] Avista no cartão\n[ 3 ] Em até 2x vezes no cartão\n[ 4 ] Em até 3x no cartão\n'))

if formaPagamento == 1:
    print('Com pagamento em dinheiro ou cheque você terá desconto de 10%,com isso valor do produto ficará em R${:.2f}'.format(precoProduto - (10 * precoProduto) / 100))
elif formaPagamento == 2:
    print('Com pagamento a vista no cartão você terá desconto de 5%,com isso valor do produto ficará em R${:.2f}'.format(precoProduto - (5 * precoProduto) / 100))
elif formaPagamento == 3:
    print('Com pagamento em 2x no cartão você pagará o valor normal do produto que é R${:.2f}'.format(precoProduto))
elif formaPagamento == 4:
    print('Com pagamento em 3x no cartão você pagará um juros de 20% em cima do valor do produto,por tanto o novo valor será R${:.2f}'.format(precoProduto + (20 * precoProduto) / 100))
else:
    print('Opção inválida,tente novamente.')

