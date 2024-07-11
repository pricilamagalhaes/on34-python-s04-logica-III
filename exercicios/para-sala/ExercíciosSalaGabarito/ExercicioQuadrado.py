# Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos
# quadrados dos elementos do vetor.

def main():
    resposta = input("Digite 10 números separados por vírgula: ")
    lista_numeros = resposta.split(",")

    soma = 0
    for numero in lista_numeros:
        quadrado = int(numero)*int(numero)
        soma = soma + quadrado
        print(quadrado)

    print("O valor final é {}".format(soma))



main()

