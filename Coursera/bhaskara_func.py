import math

def delta(a, b, c):
    return b ** 2 - 4 * a * c

def main():
    a = float(input("Digite o valor de A: "))
    b = float(input("Digite o valor de B: "))
    c = float(input("Digite o valor de C: "))
    imprime_raizes(a, b, c)

def imprime_raizes(a, b, c):
    delta = delta(a, b, c)
    if delta == 0:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        print("A única raíz é: ", raiz1)
    else:
        if delta < 0:
            print("Esta equação não possui raízes reais.")
        else:
            raiz1 = (-b + math.sqrt(delta)) / (2 * a)
            raiz2 = (-b - math.sqrt(delta)) / (2 * a)
            print("A primeira raíz é: ", raiz1)
            print("A segunda raíz é: ", raiz2)