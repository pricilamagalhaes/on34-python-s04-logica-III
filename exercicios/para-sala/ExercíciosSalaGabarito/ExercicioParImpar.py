#Faça um Programa que leia 10 números inteiros e armazene-os num vetor. 
#Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

def main():
    numeros = input("Digite 10 números separados por vírgula: ")
    numeros = numeros.split(",")
    lista_par = []
    lista_impar = []

    for n in numeros:
        if int(n) % 2 == 0:
            lista_par.append(n)
        else:
            lista_impar.append(n)
    
    print("Lista Par: {}".format(lista_par))
    print("/nLista Par: {}".format(lista_impar))

main()

