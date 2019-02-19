''''SUPERCLASS'''
class graphicObject(object):
    def __init__(self, filled, color_fill=None, color_outline=None):
        self.filled = filled
        self.color_fill = color_fill
        self.color_outline = color_outline
    
    def calculateCircle(self, radius):
        area = 3.14 * (radius ** 2)
        perimeter = 2 * 3.14 * radius
        return area, perimeter

    def calculateTriangle(self, base, heigth):
        area = (base * heigth) / 2
        length = base ** 2 + heigth ** 2
        length = length ** 2
        perimeter = heigth + base + length
        return area, perimeter

    def calculateRectangle(self, base, heigth):
        area = base * heigth
        perimeter = 2 * base + 2 * heigth
        return area, perimeter

'''SUBCLASSES'''
class Circle(graphicObject):
    def __init__(self, filled, color_fill, color_outline, radius):
        super().__init__(filled, color_fill, color_outline)
        self.radius = float(radius)
    def areaNperimeter(self):
        area, perimeter = super().calculateCircle(self.radius)
        print("Circle:\nArea: {}\nPerimeter: {}\n".format(area, perimeter))
        print('')
    def getDetails(self):
        print('Details about circle:')
        print('Filled: {}\nColor fill: {}\nColor outline: {}\nRadius: {}'.format(self.filled, self.color_fill, self.color_outline, self.radius))
        print('')

class Triangle(graphicObject):
    def __init__(self, filled, color_fill, color_outline, base, heigth):
        super().__init__(filled, color_fill, color_outline)
        self.base = float(base)
        self.heigth = float(heigth)
    def areaNperimeter(self):
        area, perimeter = super().calculateTriangle(self.base, self.heigth)
        print("Triangle:\nArea: {}\nPerimeter: {}\n".format(area, perimeter))
        print('')
    def getDetails(self):
        print('Details about triangle:')
        print('Filled: {}\nColor fill: {}\nColor outline: {}\nBase: {}\nHeigth: {}'.format(self.filled, self.color_fill, self.color_outline, self.base, self.heigth))
        print('')

class Rectangle(graphicObject):
    def __init__(self, filled, color_fill, color_outline, base, heigth):
        super().__init__(filled, color_fill, color_outline)
        self.base = float(base)
        self.heigth = float(heigth)
    def areaNperimeter(self):
        area, perimeter = super().calculateRectangle(self.base, self.heigth)
        print("Rectangle:\nArea: {}m2\nPerimeter: {}m\n".format(area, perimeter))
        print('')
    def getDetails(self):
        print('Details about rectangle:')
        print('Filled: {}\nColor fill: {}\nColor outline: {}\nBase: {}\nHeigth: {}'.format(self.filled, self.color_fill, self.color_outline, self.base, self.heigth))
        print('')

'''Creating Objects'''
def Fill():
    filled = input('Is filled? (y/n) ')
    if filled == 'y':
        filled = True
    else:
        filled = False
    if filled == True:
        color_fill = input('Color fill: ')
        color_outline = input('Color outline: ')
        return [filled, color_fill, color_outline]
    else:
        return [filled, None, None]

def createCircle():
    print("Circle details:")
    radius = input('Radius: ')
    filled, color_fill, color_outline = Fill()
    circle = Circle(filled, color_fill, color_outline, radius)
    print('Circle was created.')
    print('')
    return circle

def createTriangle():
    print("Triangle details:")
    base = input('Base: ')
    heigth = input("Heigth: ")
    filled, color_fill, color_outline = Fill()
    triangle = Triangle(filled, color_fill, color_outline, base, heigth)
    print('Triangle was created.')
    print('')
    return triangle

def createRectangle():
    print("Rectangle details:")
    base = input('Base: ')
    heigth = input("Heigth: ")
    filled, color_fill, color_outline = Fill()
    rectangle = Rectangle(filled, color_fill, color_outline, base, heigth)
    print('Rectangle was created.')
    print('')
    return rectangle

def main():
    answer = 'yes'
    while answer == 'yes':
        print('=== Objects ===')
        print('')
        rectangle = createRectangle()
        circle = createCircle()
        triangle = createTriangle()
        print('=== Details about the objects ===')
        print('')
        rectangle.getDetails()
        circle.getDetails()
        triangle.getDetails()
        print('=== Object calculations ===')
        print('')
        rectangle.areaNperimeter()
        circle.areaNperimeter()
        triangle.areaNperimeter()
        answer = input('Do you want repeat? (y/n): ')

main()