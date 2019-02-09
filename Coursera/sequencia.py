sequence = int(input("Digite quantos números tem a sequência. "))
begin = 1
soma = 1
while begin <= sequence:
    number = int(input("Digite um número a ser somado: "))
    begin += 1
    soma += number
print(soma)