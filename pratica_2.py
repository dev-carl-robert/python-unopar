estoque_1 = {
    "produto": ["Camiseta", "Calça Jeans", "Tênis", "Bermuda", "Jaqueta"],
    "quantidade": [5, 12, 3, 8, 6],
    "reabastecido": ["false", "true", "false", "true", "false"]
}

estoque_2 = {
    "produto": ["Boné", "Meias", "Tênis", "Cinto", "Saco de Roupas"],
    "quantidade": [15, 20, 2, 18, 5],
    "reabastecido": ["true", "true", "false", "true", "false"]
}

# Combine os dois dicionários de produtos.
lista_estoque1 = list(zip(estoque_1["produto"], estoque_1["quantidade"], estoque_1["reabastecido"]))
lista_estoque2 = list(zip(estoque_2["produto"], estoque_2["quantidade"], estoque_2["reabastecido"]))
estoque_geral = lista_estoque1 + lista_estoque2
for produto, quantidade, reabastecido in estoque_geral:
    print(f"produto: {produto} \nquantidade: {quantidade} \nreabastecido? {'sim' if reabastecido == 'true' else 'não'}\n")
# Liste os produtos que têm quantidade abaixo de 10 (considerados "críticos").
print("produtos criticos")
for produto, quantidade, reabastecido in estoque_geral:
    print(f"produto: {produto} \nquantidade: {quantidade} \nsituação: {'critico' if quantidade < 10 else 'normal'} \nreabastecido? {'sim' if reabastecido == 'true' else 'não'}\n")
    produtos_criticos = [produto for produto, quantidade, reabastecido in estoque_geral if quantidade < 10]
# Liste os produtos que têm quantidade igual ou superior a 10 (considerados "normais").
print("produtos normais")
for produto, quantidade, reabastecido in estoque_geral:
    print(f"produto: {produto} \nquantidade: {quantidade} \nsituação: {'critico' if quantidade < 10 else 'normal'} \nreabastecido? {'sim' if reabastecido == 'true' else 'não'}\n")
    normais = [produto for produto, quantidade, reabastecido in estoque_geral if quantidade >= 10]
# Encontre o produto com a menor quantidade no estoque.
produto_menor_quantidade = min(estoque_geral, key=lambda x: x[1])

print("\n--- Produto com Menor Quantidade ---")
print(f"produto: {produto_menor_quantidade[0]} \nquantidade: {produto_menor_quantidade[1]} \nreabastecido? {'sim' if produto_menor_quantidade[2] == 'true' else 'não'}")
# Imprima as informações dos produtos com a menor quantidade.