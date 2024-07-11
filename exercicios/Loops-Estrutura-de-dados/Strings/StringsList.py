def palavra_contem(nome, letra):
    #percorrendo a palavra
    if nome[0] == letra:
        print("O nome '{}' contém a letra '{}'".format(nome, letra))        
        
    elif nome[1] == letra: 
        print("O nome '{}' contém a letra '{}'".format(nome, letra))
        
    elif nome[2] == letra:
        print("O nome '{}' contém a letra '{}'".format(nome, letra))
        
    elif nome[3] == letra:
        print("O nome '{}' contém a letra '{}'".format(nome, letra))
        
    elif nome[4] == letra:
        print("O nome '{}' contém a letra '{}'".format(nome, letra))
    
    else:
        print("O nome '{}' não contém a letra '{}'".format(nome, letra))
    


palavra_contem("Maria", "a")
palavra_contem("Maria", "c")


