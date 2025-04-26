texto = """No dia mais frio, na noite mais densa
           O mal sucumbirá, ante a minha presença
           Todo aquele que venera o mal
           Há de penar, quando o poder do lanterna verde enfrentar"""

texto1 = "lema dos lanternas verdes"


# verifica se a palavra está no texto
for x in texto:
    if "mal" in texto:
       print("Há")
    break

#concatena duas sequencias
print(f"{texto1} : \n {texto}") 

print(f"Tamanho do texto = {len(texto)}")
print(f"Mal in texto = {'mal' in texto}")
print(f"Quantidade de y no texto = {texto.count('mal')}")
print(f"As 5 primeiras letras são: {texto[0:6]}")

print(texto.upper())
print(texto.replace("mal", 'bem'))

palavra = texto1.split()
print(f"Palavras: {palavra}")
print(f"Palavras: {len(palavra)}")

# listas
print("compreensao de listas")

lanternas = ["verde", "azul", "amarela", "laranja", "vermelha", "roxa", "negra", "branca"]
print(lanternas)
lanternas.append("Dc")
print(lanternas)
lanternas.pop()
print(lanternas)

# compreensao de listas
print("compreensao de listas")
lanternas = [itens.upper() for itens in lanternas]
print(lanternas)

# Funções map() e filter()
print("Funções map() e filter()")
