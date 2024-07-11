produtos_venda = {
    "blusa": 10,
    "calça": 20,
    "short": 15,
    "vestido": 30,
    "sapato": 25
}

#chegou um produto novo, vamos adicionar
produtos_venda["meia"] = 5

#acabou o short, precisamos remover
produtos_venda.pop("short")

#tirar o ultimo item
produtos_venda.popitem()

#meu cliente comprou uma blusa, quanto ele gastou?
print(produtos_venda["blusa"])

#meu cliente adicionou esses itens na compra calca, sapato e vestido, qual o novo valor?
valor_total = produtos_venda["blusa"] + produtos_venda["calça"] + produtos_venda["sapato"] + produtos_venda["vestido"]
print(valor_total)

#vestido mudou de valor, agora é 45
produtos_venda["vestido"] = 45
print(produtos_venda)

#todos os itens tiveram um aumento de 10 reais
for chave in produtos_venda.keys():
    produtos_venda[chave] += 10


#criei um item conjunto, o valor dele é da calca e da blusa somados
produtos_venda["conjunto"] = produtos_venda["calça"] + produtos_venda["blusa"]
print(produtos_venda)

#quero saber se tem blusa no meu dicionario
print("blusa" in produtos_venda)
print("blsa" in produtos_venda)
