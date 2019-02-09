def main():
    number = int(input("n: "))
    total = 0
    list_primo = []
    while number != 0:
        primo = eprimo(number)
        if primo:
            if number not in list_primo:
                total += 1
                list_primo.append(number)
        number = int(input("n: "))
    print("Total de números primos digitados: {}".format(total))
    print("E os números foram: {}".format(list_primo))


def eprimo(number):
    index = 1
    vezes = 0
    while index <= number:
        if number % index == 0:
            vezes += 1
        index += 1
    if vezes == 2:
        return True
    else:
        return False

main()