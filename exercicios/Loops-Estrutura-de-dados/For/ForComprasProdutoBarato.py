
produtos = {"celular": [1000, 1300],
            "notebook": [2000, 2100] }

total = 0

for valores_produtos in produtos.values():
    for valor_produto in valores_produtos:
        total += valor_produto
        
print(total)






   
  
