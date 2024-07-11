def main():
    frutas = ["abacaxi"]

    #append - "uva"
    frutas.append("uva")

    #extend - ["morango", "abacate", "cereja"]
    frutas.extend(["morango", "abacate", "cereja"]) 
    
    #frutas[1]
    print(frutas[4])

    #index
    print(frutas.index("abacate"))

    #sort
    frutas.sort(reverse=True)

    #len
    print(len(frutas))

    #pop
    frutas.pop(1)

    #erro comum
    frutas[34]
    
    print(frutas)

main()




