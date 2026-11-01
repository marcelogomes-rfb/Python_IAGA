####Faça um programa para ler um número inteiro que representa o tamanho de uma matriz
#  quadrada. Apresente esta matriz como mostrado na coluna “Resultados”. Observe que as
#  bordas da matriz são feitas por asteriscos (*) e a parte central por símbolos de arroba (@).
num = int (input ())
for i in range (num):
    for j in range (num):
        if (i == 0 or i == num - 1 or j == 0 or j == num - 1):  
            print("* ", end="")
        else:
            print("@ ", end="")
    print()