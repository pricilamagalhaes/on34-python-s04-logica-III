def main():
    frutas_mercado = {"banana", "ameixa", "cereja", "abacaxi"}
    frutas_feira = {"banana", "cereja", "caqui", "kiwi"}

    frutas_mercado.add("banana")
    frutas_mercado.add("morango")

    print("\nUnião(+)")
    print(frutas_feira.union(frutas_mercado))
    
    print("\nInterseccao")
    print(frutas_feira.intersection(frutas_mercado))    
        
    print("\nDiferenca(-)")
    print(frutas_feira.difference(frutas_mercado))    
    print(frutas_mercado.difference(frutas_feira))

    print("\nFrutas mercado: {}".format(frutas_mercado))
    print("Frutas feira: {}".format(frutas_feira))


main()