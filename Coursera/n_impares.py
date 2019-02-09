n = int(input("Digite o valor de n: "))
numero = 1
n_impar = 1
while n_impar <= n:
    if numero % 2 != 0:
        print(numero)
        n_impar = n_impar + 1
        numero = numero + 1
    else:
        numero = numero + 1
        