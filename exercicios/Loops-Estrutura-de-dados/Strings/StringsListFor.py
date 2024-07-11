def palavra_contem(nome, letra):
    #percorrendo a palavra
    for x in nome:
        if x == letra:
            print("O nome '{}' contém a letra '{}'".format(nome, letra))
            break
    else:
        print("O nome '{}' não contém a letra '{}'".format(nome, letra))

def quantidade_palavra(frase, palavra):
    frase_dividida = frase.split(" ")
    quantidade = 0
    for x in frase_dividida:
        if x == palavra:
            quantidade += 1
    print("Nessa frase a palavra '{}' se repete {} vezes".format(palavra, quantidade))

    

def main():
    #palavra
    palavra_contem("Eduarda", "a")
    palavra_contem("Eduarda", "c")

    #frase
    quantidade_palavra("A menina está procurando o gato que está na árvore", "está")
    quantidade_palavra("A menina está procurando o gato que está na árvore", "cachorro")

main()