def nome_simples():
    alunas = ["eduarda", "ana", "maria", "paula"]
    '''for item in alunas:
        print(item)'''
    [print(item) for item in alunas]

def numeros():
    numeros = [1,2,3,4]
    [print(item+1) for item in numeros]

numeros()

