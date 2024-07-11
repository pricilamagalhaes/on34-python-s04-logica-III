# Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos
# quadrados dos elementos do vetor.


def main():
    numeros = input("Digite 10 numeros separados por virgula: ")
    lista_numeros = []

    # Converte os números para inteiros e adiciona à lista
    for num in numeros.split(","):
        lista_numeros.append(int(num))

    
    soma= 0
    # Calcula o quadrado de cada número e exibe
    # Calcula a soma  e imprime a soma
    for num in lista_numeros:
        quadrado = num ** 2
        print(f"O quadrado de {num} é {quadrado}")
        soma = soma + quadrado
        print (f"o valor da soma dos quadrados é: ", soma)


main()