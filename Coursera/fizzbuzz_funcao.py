def fizz(n):
    fizzr = False
    if n % 3 == 0 and n % 5 != 0:
        fizzr = True
    return fizzr

def buzz(n):
    buzzr = False
    if n % 5 == 0 and n % 3 != 0:
        buzzr = True
    return buzzr

def fizzbuzz(n):
    fizzn = fizz(n)
    buzzn = buzz(n)
    if fizzn:
        return "Fizz"
    elif buzzn:
        return "Buzz"
    elif n % 5 == 0 and n % 3 == 0:
        return "FizzBuzz"
    elif n % 5 != 0 and n % 3 != 0:
        return n
    


