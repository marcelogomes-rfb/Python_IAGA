###Faça um programa para ler uma String e apresente todos os caracteres desta String 3 (três)
#  vezes na tela do computador. Observe o resultado final na coluna “Resultados”.
pal = str(input())
for i in range (3):
    for i in pal:
        print (f'{i}', end=" ")
    print ()