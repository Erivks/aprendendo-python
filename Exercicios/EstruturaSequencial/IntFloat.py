integers = input("Type two integer numbers: ").split()
floating = float(input("Now, type one decimal number: "))
iOne, iTwo = list(map(int, integers))

multiplication = ((iOne * 2) * (iTwo / 2))
sumResult = ((iOne * 3) + floating)
cube = floating ** 3

print("Multiplication:\n\n(({} * 2) * ({} / 2)) = {}\n".format(iOne, iTwo, multiplication))
print("Sum result:\n\n(({} * 3) + {}) = {}\n".format(iOne, floating, sumResult))
print("Cube:\n\n{}^3 = {}\n".format(floating, cube))

