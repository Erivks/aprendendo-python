#Criar uma class que cria um retângulo
class Rectangle(object):
    def __init__(self, length, width):
        self.length = int(length)
        self.width = int(width)

    def changeSides(self, length, width):
        self.length = int(length)
        self.width = int(width)

    def returnSides(self):
        print("Length: {}\nWidth: {}".format(self.length, self.width))

    def calculateArea(self):
        return self.length * self.width

    def calculatePerimeter(self):
        return 2 * self.length + 2 * self.width
    
    def calculateFloor(self, m, m2):
        Meters = m2 / (m * m)
        Percent = Meters * 10 / 100
        Floor = Meters + Percent
        return Floor

class Floor(object):
    def __init__(self, cm):
        self.cm = int(cm)
    
    def cmTom(self):
        return self.cm / 100

def main():
    length = input('Report the length: ')
    width = input('Report the width: ')
    rectangle = Rectangle(length, width)
    print('Ok, the rectangle was created.\nAnd these are it sides:')
    rectangle.returnSides()
    answer = input('Do you would want change any value? (y/n)')
    if answer == 'y':
        length = input('Report the new value for length: ')
        width = input('And the new value for width: ')
        rectangle.changeSides(length, width)
        print('The values were changed.')
    else:
        print("Ok, so let's continue.")
    print('These are the values for:')
    print('Area:', rectangle.calculateArea())
    print('Perimeter:', rectangle.calculatePerimeter())
    cm = input('So now Report the floor value in cm: ')
    floor = Floor(cm)
    mfloor = floor.cmTom()
    m2 = rectangle.calculateArea()
    floors = rectangle.calculateFloor(mfloor, m2)
    print('This is the quantity needed of floors for the rectangle: {}'.format(int(floors)))

main()
