def primo(k):
    i = 1
    vezes = 0
    while i <= k:
        resto = k % i
        if resto == 0:
            vezes = vezes + 1
        i = i + 1
    if vezes == 2:
        return True
    else:
        return False

def maior_primo(n):
    maior = 0
    achou = False
    while achou != True:
        numero = primo(n)
        if numero == True:
            maior = n
            achou = True
        n = n - 1
    return maior

print(maior_primo(7))