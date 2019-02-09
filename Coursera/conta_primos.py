def eprimo(number):
    index = 1
    vezes = 0
    while index <= number:
        if number % index == 0:
            vezes += 1
        index += 1
    if vezes == 2:
        return True
    else:
        return False

def n_primos(number):
    index = 2
    quantidade = 0
    while index <= number:
        if eprimo(index):
            quantidade += 1
        index += 1
    return quantidade

print(n_primos(108))