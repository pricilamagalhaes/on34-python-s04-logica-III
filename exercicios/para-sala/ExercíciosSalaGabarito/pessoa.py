#Crie um dicionário com os pares de chave-valor: "nome": "Ana", "idade": 25.
dicionario = {
    "nome": "Ana",
    "idade": 25
}

#Acesse o valor associado à chave "nome".
print(dicionario["nome"])

#Adicione um novo par de chave-valor: "cidade": "São Paulo".
dicionario["cidade"] = "Sao Paulo"
print(dicionario)

#Verifique se a chave "idade" está no dicionário.
print("idade" in dicionario)
print("estado" in dicionario)



#pergunte a idade de uma pessoa e adicione em um dicionario
dicionario_pessoa_3 = {
    "nome": "Paulo"
}

idade = input("Digite sua idade:")

dicionario_pessoa_3["idade"] = idade

print(dicionario_pessoa_3)

#Crie uma lista de dicionários, onde cada dicionário representa uma pessoa com "nome" e "idade".
dicionario_pessoa_2 = {
    "nome": "Pedro",
    "idade": 23
}

lista_dicionario = [dicionario, dicionario_pessoa_2]

print(lista_dicionario)

#Acesse o nome da segunda pessoa na lista.
#Lembrando que para pegar a segunda pessoa usamos o indice 1 pois sempre comeca do 0
nome_segunda_pessoa = lista_dicionario[1]["nome"]
print(nome_segunda_pessoa)

