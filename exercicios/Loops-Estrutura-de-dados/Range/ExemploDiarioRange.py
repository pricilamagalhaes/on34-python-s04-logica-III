# Exemplo Iteração

# Quero criar um diario para poder escrever sobre meus dias  
def diario(dia):     
    # Crio a string que contém a data
    data = "{} de janeiro".format(dia)
    return data



def print_diario():
    janeiro = ""
    for dia in range(1,32):
       janeiro += diario(dia)
       janeiro += "\n____________________________\n"
    print(janeiro)

print_diario()
















