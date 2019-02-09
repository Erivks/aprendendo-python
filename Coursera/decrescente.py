#definições
decrescente = True
anterior = int(input("O primeiro número da sequência: "))
valor = 1

#condição de parada e repetição
while valor != 0 and decrescente:
    valor = int(input("O próximo número da sequência: "))
    if valor > anterior:
        decrescente = False #para a repetição
    anterior = valor

#resposta final
if decrescente:
    print("Esta é uma sequência decrescente.")
else:
    print("Esta não é uma sequência decrescente.")
