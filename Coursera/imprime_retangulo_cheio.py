largura = int(input("digite a largura: "))
altura =  int(input("digite a altura: "))

cont = 1
i = 1
while cont <= altura:
    i = 1
    while i <= largura:
        print("#", end="")
        i = i + 1
    print("")
    cont = cont + 1