###FFaça um programa para ler uma String e apresente todos as palavras desta String. Leve em
#  consideração que entre as palavras existem um, e somente um, caractere espaço. Veja, também, que o ponto final não faz parte da última palavra. Observe o resultado final
#  na coluna “Resultados”.
string = str(input()) # insere a string
palavras = string.split # separa as palavras por espaço
print (f'Existem', end= " ")
print (len ({palavras}), end= " ")
print ("palavras, são elas:")
for i in palavras:
    print (f'{i }a. palavra =', end= " ")
    print (i)
