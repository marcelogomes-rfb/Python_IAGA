####Faça um programa para ler um valor monetário (R$) de um produto e calcule
#  um desconto de 10% se o valor do produto for inferior a R$ 5.000,00; o desconto a ser calculado, em caso
#  contrário, deverá ser de 15%. Calcule, também, o valor final do produto e apresente os
#  valores como mostrado na coluna 'Resultados'.
valor_Produto = float (input())
if valor_Produto < 5000.00:
    desconto = 10
    valor_Desconto= valor_Produto * 0.10
else:
    desconto = 15
    valor_Desconto= valor_Produto * 0.15
valor_Final = valor_Produto - valor_Desconto
print (f'Valor do Produto        = R$ {valor_Produto:.2f}')
print (f'Valor do Desconto ({desconto}%) = R$ {valor_Desconto:.2f}')
print (f'Valor Final             = R$ {valor_Final:.2f}')