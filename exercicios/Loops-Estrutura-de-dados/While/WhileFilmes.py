def main():
    meus_filmes = ["Matrix", "Harry Potter", "Procurando Nemo", "Titanic"]
    filmes(meus_filmes)

def filmes(meus_filmes):
    indice = 0
    while indice < len(meus_filmes):
        print(meus_filmes[indice])
        indice = indice + 1