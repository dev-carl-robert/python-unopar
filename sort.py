# versao complexa (sorted)
print(60* "=")
print('versao complexa (sorted)')
def executar_ordenação(lista):
    n = len(lista)
    for i in range (0, n):
        index_menor = i
        for j in range(i+1, n):
            if lista[j] < lista[i]:
                index_menor = j
            lista[i], lista[j] = lista[j], lista[i]
        print(lista)

lista = [5, 9, 2, -1]
executar_ordenação(lista)

# versao resumida (sorted)
print(60* "=")
print("versao resumida (sorted)")
numeros = [5, 2, 9, 1]
nova_lista = sorted(numeros)
print(nova_lista)  # [1, 2, 5, 9]
print(numeros)     # [5, 2, 9, 1] (não mudou)



# (sort)
print(60* "=")
print('sort')

numeros = [5, 2, 9, 1]
numeros.sort()
print(numeros)  # [1, 2, 5, 9]

# (sort decrescente)
print(60* "=")
print('sort decrescente')

numeros = [5, 2, 9, 1]
numeros.sort(reverse=True)
print(numeros)  # [9, 5, 2, 1]

# Ordenar palavras por tamanho:
print(60* "=")
print('ordenação por tamanho')
palavras = ['banana', 'abacaxi', 'uva']
palavras.sort(key=len)
print(palavras)  # ['uva', 'banana', 'abacaxi'

# Ordenar lista de dicionários pelo valor de uma chave:
print(60* "=")
print('Ordenar lista de dicionários pelo valor de uma chave:')
pessoas = [{'nome': 'Ana', 'idade': 23}, {'nome': 'João', 'idade': 20}]
pessoas.sort(key=lambda pessoa: pessoa['idade'])
print(pessoas)  # João primeiro, depois Ana

# buble sort
print(60* "=")
print('Buble sort')
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]  # Troca
    return lista

# Exemplo
numeros = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(numeros))  # [11, 12, 22, 25, 34, 64, 90]

# selection sort
print(60* "=")
print('selection sort')
def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

# Exemplo
numeros = [64, 25, 12, 22, 11]
print(selection_sort(numeros))  # [11, 12, 22, 25, 64]

# merge sort
print(60 * '=')
print("merge sort")
def merge_sort(lista):
    if len(lista) > 1:
        meio = len(lista) // 2
        esquerda = lista[:meio]
        direita = lista[meio:]

        merge_sort(esquerda)
        merge_sort(direita)

        i = j = k = 0

        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                lista[k] = esquerda[i]
                i += 1
            else:
                lista[k] = direita[j]
                j += 1
            k += 1

        while i < len(esquerda):
            lista[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            lista[k] = direita[j]
            j += 1
            k += 1

    return lista

# Exemplo
numeros = [38, 27, 43, 3, 9, 82, 10]
print(merge_sort(numeros))  # [3, 9, 10, 27, 38, 43, 82]


print(60* '=')
print("quick sort")
# quick sort
def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivo = lista[0]
        menores = [x for x in lista[1:] if x <= pivo]
        maiores = [x for x in lista[1:] if x > pivo]
        return quick_sort(menores) + [pivo] + quick_sort(maiores)

# Exemplo
numeros = [10, 7, 8, 9, 1, 5]
print(quick_sort(numeros))  # [1, 5, 7, 8, 9, 10]
