#Criar um class que modele um quadrado
class Square(object):
    def __init__(self, side):
        self.side = int(side)
    def setSide(self, side): 
        self.side = int(side)
    def returnSide(self):
        return self.side
    def calculateArea(self):
        return self.side ** 2

def main():
    side_of_sq = input("Report the square's side: ")
    square = Square(side_of_sq)
    print("Square's area: {}".format(square.calculateArea()))
    answer = input("Do you want change the square's side? (y/n) ")
    if answer == 'y':
        side_of_sq = input("Report the new square's side: ")
        square.setSide(side_of_sq)
        print("This is the new square's side: {}".format(square.returnSide()))
        print("And this is the area of the square: {}".format(square.calculateArea()))
    else:
        print("The square's side: {}".format(square.returnSide()))

main()