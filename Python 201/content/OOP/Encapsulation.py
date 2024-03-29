class Person:
    # documentation
    '''
        Adding `__` to variables declared in __init__
        makes the variable encapsualted. Innacessible publicly.

        Setters and getters, are the ways in which these private vars can be accessed.

        Protect accidental changes in data. But does NOT provide security.
     '''

    class_attribute_1 =  True

    def __init__(self, name, age):
        self.name =  name
        self.__age  = age #encapsualted variable by adding `__`
    
    def get_age(self):
        return self.__age
    
    def set_age(self, newage):
        self.__age =  newage

    def print_age(self):
        print("age: {}".format((self.get_age())))
    
    def print_name(self):
        print("name: {}".format(self.name))
    
    def change_name(self, new_name='boby'):
        self.name =  new_name
        self.print_name()

bob = Person(name='bob',age=30)
bob.print_age() #30
bob.set_age(31)
bob.print_age() #31

# encapsulation does not provide security.
print(bob.__dict__) # {'name': 'bob', '_Person__age': 31}
bob._Person__age = 40
bob.print_age() #40
