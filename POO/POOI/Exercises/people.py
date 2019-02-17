#Creating the class 'people'
class People(object):
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = int(age)
        self.weight = float(weight)
        self.height = float(height)    
    def growOld(self, age):
        self.age += int(age)
        if self.age < 21:
            self.height += 0.05
    def fatten(self, kilos):
        self.weight += float(kilos)
    def returnData(self):
        print('About you: ')
        print("Name: {}\nAge: {}\nWeight: {}\nHeight: {}".format(self.name, self.age, self.weight, self.height))

def main():
    print('Report your personal data:')
    name = input('Name: ')
    age = input('Age: ')
    weight = input('Weight: ')
    height = input('Height: ')
    people = People(name, age, weight, height)
    people.returnData()
    old = input('Now, tell me how old you want to grow old: ')
    people.growOld(old)
    people.returnData()
    kilos = input('Tell me how kilos you want to fatten: ')
    people.fatten(kilos)
    people.returnData()

main()