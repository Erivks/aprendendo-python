class Rectangle(object):
    def __init__(self, length, heigth, point):
        self.length = float(length)
        self.heigth = float(heigth)
        self.point = point
    
    def setSide(self, length, heigth):
        self.length = float(length)
        self.heigth = float(heigth)
    
    def returnDataRect(self):
        print("Rectangle:\nLength: {}\nHeigth: {}".format(self.length, self.heigth))
    
    def returnDataPoint(self):
        self.point.x = self.length / 2
        self.point.y = self.heigth / 2
        print("Point:\nX: {}\nY: {}".format(self.point.x, self.point.y))

class Point(object):
    def __init__(self):
        self.x = 0 
        self.y = 0

def main():
    length, heigth = input('Report the length value and heigth value: ').split(' ')
    point = Point()
    rectangle = Rectangle(length, heigth, point)
    rectangle.returnDataRect()
    answer = input("Do you want change something? (y/n) ")
    if answer == 'y':
        length, heigth = input('Report the length value and heigth value: ').split(' ')
        rectangle.setSide(length, heigth)
    else:
        print('Ok..')
    print("This is the center of rectangle:")
    rectangle.returnDataPoint()

main()