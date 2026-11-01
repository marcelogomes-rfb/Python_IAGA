###Faça um programa para ler um valor monetário (R$) de um produto e calcule um desconto fixo de 10%.
#  Calcule também o valor final do produto.
#  Apresente os valores como apresentado na coluna “Resultados”.
valor_Produto = float (input())
desconto = valor_Produto * 0.1
valor_Final = valor_Produto - desconto
print (f'Valor do Produto  = R$ {valor_Produto:.2f}')
print (f'Valor do Desconto = R$ {desconto:.2f}')
print (f'Valor Final       = R$ {valor_Final:.2f}')