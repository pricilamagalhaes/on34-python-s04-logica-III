# Exemplo Iteração

# Quero criar um diario para poder escrever sobre meus dias  
def diario(dia):     
    # Crio a string que contém a data
    data = "{} de janeiro".format(dia)
    data += "\n ____________________________________\n"
    return data


def main():
    janeiro = ""
    janeiro += diario(1)
    janeiro += diario(2)    
    janeiro += diario(3)    
    janeiro += diario(4)   
    janeiro += diario(5)
    janeiro += diario(6)    
    janeiro += diario(7)    
    janeiro += diario(8)    
    janeiro += diario(9)
    janeiro += diario(10)    
    #... janeiro += diario(31)    
    print(janeiro)

main()