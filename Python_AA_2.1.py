###Faça um programa que leia um valor inteiro do teclado (variável “item”) e a seguir
#  implemente a rotina de busca sequencial: do primeiro elemento da Lista até
#  encontrar; ou até o final da Lista e não encontrar. Mostre as posições juntas dos respectivos elementos da Lista
#  “a” e, finalizando, com o resultado da busca: encontrou na posição tal; ou não encontrou
#  “item” na Lista “a”. Observe o resultado final na coluna “Resultados”.
item = int(input())
lista = [10, 2, 7, 8, 5, 3, 22, 17, 18]
if item in lista:
    indice = lista.index(item)
    print ("{0:10, 1:2, 2:7, 3:8, 4:5, 5:3, 6:22, 7:17, 8:18}")
    print ()
    print (f'Item: {item}, foi encontrado na posicao {indice}.')
else:
    print ("{0:10, 1:2, 2:7, 3:8, 4:5, 5:3, 6:22, 7:17, 8:18}")
    print ()
    print (f'Item: {item}, \"não\" foi encontrado.')