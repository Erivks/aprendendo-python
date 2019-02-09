def e_hipotenusa(c1, c2, h):
    if (c1 * c1) + (c2 * c2) == (h * h):
        return True
    else:
        return False

def soma_hipotenusas(numero):
    inicio = 1
    soma = 0
    while inicio <= numero:
        cateto1 = 1
        while cateto1 < numero:
            cateto2 = 1
            while cateto2 < numero:
                if e_hipotenusa(cateto1, cateto2, inicio):
                    print("{}^2 + {}^2 = {}^2".format(cateto1, cateto2, inicio))
                    soma = soma + inicio
                    cateto1 = numero
                    break
                cateto2 += 1
            cateto1 += 1
        inicio += 1    
    return soma

print(soma_hipotenusas(80))