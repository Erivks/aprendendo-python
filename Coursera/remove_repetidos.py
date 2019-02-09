def remove_repetidos(lista):
    nova_lista = []
    for value in lista:
        for indice in range(len(lista)):
            if lista[indice] == value:
                if value not in nova_lista:
                    nova_lista.append(value)
                else:
                    break 
    nova_lista.sort()
    return nova_lista

lista = [8, 8, 4, 3, 2, 5]

print(remove_repetidos(lista))
