carregamento_1 = {
    "produto": ["Teclado Gamer", "Mouse Sem Fio", "Monitor 24''", "Cadeira Escritório", "Fone Bluetooth"],
    "quantidade": [10, 15, 7, 5, 20],
    "conferido": ["true", "false", "true", "false", "true"]
}
carregamento_2 = {
    "produto": ["Impressora", "Webcam HD", "Notebook", "HD Externo", "Mousepad XXL"],
    "quantidade": [3, 12, 8, 6, 18],
    "conferido": ["false", "true", "false", "true", "false"]
}


# Juntar os dois carregamentos em uma única lista.
list_1 = list(zip(carregamento_1["produto"], carregamento_1["quantidade"], carregamento_1["conferido"]))
list_2 = list(zip(carregamento_2["produto"], carregamento_2["quantidade"], carregamento_2["conferido"]))
lista_completa = list_1 + list_2
# Listar apenas os produtos ainda não conferidos.
produtos_nao_conferidos = [produto for produto, quantidade, conferido in lista_completa if conferido == "false"]
print(produtos_nao_conferidos)
# Mostrar os produtos que já foram conferidos.
produtos_conferidos = [produto for produto, quantidade, conferido in lista_completa if conferido == "true"]
print(produtos_conferidos)
# Imprimir o primeiro produto que falta conferir.
for produto, quantidade, conferido in lista_completa:
    if conferido == "false":
        print(f"Produto a conferir: {produto} ({quantidade})")
        break   