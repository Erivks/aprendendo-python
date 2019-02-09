def maior_elemento(lista):
    for index in range(len(lista)):
        if index == len(lista):
           if lista[index] > lista[index - 1]:
               maior = lista[index] 
               break
        if lista[index] > lista[index + 1]:
            maior = lista[index]
    return maior

lista = [7, 5, 3]
print(maior_elemento(lista))
