#definição
mycard = int(input("Inform us your credit card number: "))
found_card = False
checked_card = 1
#repetição e condição de parada
while checked_card != 0 and not found_card:
    checked_card = int(input("Inform us a new credit card number for searching: "))
    if checked_card == mycard:
        found_card = True
#resposta
if found_card:
    print("We find your card here.")
else:
    print("Sorry we couldn't find your card here.")