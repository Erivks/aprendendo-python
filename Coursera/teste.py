def maxima(temps):
    maximo = max(temps)
    return maximo 

def minima(temps):
    minimo = min(temps)
    return minimo


#testes automatizados
def testa_minima():
    print("Iniciando os testes...")
    print("Teste um: ")
    testes([0], 0)
    print("Teste dois: ")
    testes([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)
    print("Teste três: ")
    testes([30, 27, 25, 26, 29, 31, 32, 30, 33, 29, 24, 30, 27, 24, 25, 22, 22], 22)
    print("Teste quatro: ")
    testes([-6, -9, -55, 0, -7, -456], -456)
    print("Finalizando teste...")

def testes(temps, valor_esperado):
    valor = minima(temps)
    if minima(temps) != valor_esperado:
        print("Valor errado para array {}".format(temps))
        print("Valor esperado: {}".format(valor_esperado))
        print("Valor calculado: {}".format(valor))
    else:
        print("Teste realizado com sucesso!")
        print("O resultado foi {}".format(valor))

testa_minima()