def fatorial(numero):
    fat = 1
    i = 1
    while i <= numero:
        fat = fat * i
        i = i + 1
    return fat

def testa_fatorial():
    if fatorial(1) == 1:
        print("Funciona para 1")
    else:
        print("Não funciona para 1")
    if fatorial(2) == 2:
        print("Funciona para 2")
    else:
        print("Não funciona para 2")
    if fatorial(0) == 1:
        print("Funciona para 0")
    else:
        print("Não funciona para 0")
    if fatorial(5) == 120:
        print("Funciona para 5")
    else:
        print("Não funciona para 5")

#Coeficiente Binomial
#(n, k) = n! / (k! * (n - k)!)

def numero_binomial(n, k):
    numero_binomial = fatorial(n) / (fatorial(k) * fatorial(n - k)) 
    return numero_binomial

testa_fatorial()
print(numero_binomial(5, 3))