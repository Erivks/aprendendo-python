x = int(input("Digite um número inteiro: "))
verificar = False
anterior = False
iguais = False
while x != 0:
    resto = x % 10
    x = x // 10
    if verificar == True:
        if resto == anterior:
            iguais = True
            x = 0
        else:
            iguais = False
    verificar = True
    anterior = resto

if iguais:
    print("sim")
else:
    print("não")