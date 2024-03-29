class Person:
    # documentation
    'Person Base class'

    class_attribute_1 =  True

    def __init__(self, name, age):
        self.name =  name
        self.age  = age

    def print_name(self):
        print("name: {}".format(self.name))
    
    def change_name(self, new_name='boby'):
        self.name =  new_name
        self.print_name()


class Hacker(Person): #This class inherits from the base class Person
    def __init__(self, name, age, cves):
        super().__init__(name, age) #supper, reffer to base class
        self.cves = cves

    def print_cves(self):
        print(self.cves)

bread =  Hacker(name='croissant',age=30, cves=5)

bread.print_name() # Access base class methods
bread.print_cves() # Access class specific method

print(issubclass(Hacker,Person)) #true
print(isinstance(bread, Hacker)) #true
