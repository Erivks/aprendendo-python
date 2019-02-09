numero = int(input("Digite um número inteiro: "))
cont = 1
vezes = 0
while cont <= numero:
    primo = numero % cont
    cont = cont + 1
    if (primo == 0):
        vezes = vezes + 1

if (vezes == 2):
    print("primo")
else:
    print("não primo")