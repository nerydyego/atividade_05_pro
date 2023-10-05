


def soma(var1, var2):
    resultado = int(var1 + var2)
    return resultado

def subtracao(var1, var2):
    resultado = var1 - var2
    return resultado

def multiplicacao(var1, var2):
    resultado = var1 * var2
    return resultado

def divisao(var1, var2):
    resultado = int(var1 / var2)
    return resultado

var1 = int(input("Informe O primeiro valor: "))
var2 = int(input("Informe O segundo valor: "))
funcao = input("Informe a função\n"
               "1 - soma\n"
               "2 - subtracao\n"
               "3 - multiplicação\n"
               "4 - divisão: " )
if funcao == 1:
    print (soma(var1, var2))
elif funcao == 2:
    print (subtracao(var1, var2))
elif funcao == 3:
    print (multiplicacao(var1, var2))
else :
    print (divisao(var1, var2))
