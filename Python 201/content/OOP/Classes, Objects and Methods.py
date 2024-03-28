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

print(Person.class_attribute_1)

bob  =  Person('bob',30)
alice  =  Person('alice',20)

print(bob.class_attribute_1)
bob.class_attribute_1 = False
print(bob.class_attribute_1)
print(alice.class_attribute_1)

print(bob.name)
print(bob.__class__)

print(hasattr(bob, 'age'))
print(getattr(bob, 'age'))

print(hasattr(bob, 'asd'))
setattr(bob,'asd',100)
print(hasattr(bob, 'asd'))
print(getattr(bob, 'asd'))

delattr(bob,'asd')
print(hasattr(bob, 'asd'))

bob.print_name()
bob.change_name()
bob.change_name('fredy')
bob.name = "marley"
bob.print_name()

del bob.name
try:
    print(bob.name)
except AttributeError:
    print(AttributeError, "'Person' object has no attribute 'name'")

print(Person.__dict__) #name space dictionary
print(Person.__doc__)
print(Person.__name__)
print(Person.__module__)
