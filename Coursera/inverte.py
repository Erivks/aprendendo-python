number = int(input("Digite um número: "))
lista = []
while number != 0:
    lista.append(number)
    number = int(input("Digite um número: "))

for index in range((len(lista) - 1), -1, -1):
    print(lista[index])