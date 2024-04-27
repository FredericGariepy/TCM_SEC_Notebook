class Person:
    # documentation
    'Person Base class'

    is_hacker = True

    def __init__(self, name, age):
        self.__name = name
        self.__age = age  # having .__ makes the attribute private

    def print_name(self):
        print("name: {}".format(self.__name))

    @classmethod
    def dangerous(cls): # 'cls' is a convention (='class')
        return cls.is_hacker

    @classmethod
    def person_factory(cls):
        return cls('factory-made',0)

    @staticmethod
    def static_method():
        print("subclasses do not change me!")

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @age.deleter
    def age(self):
        del self.__age

person = Person('fred', 30)
print(person.name)  # Output: fred
try:
    del person.age
    print(person.age)  # This will raise an AttributeError
except AttributeError as e:
    print("age has been deleted", e)

print(Person.is_hacker) # used to access the class atribute

premade1 = Person.person_factory()
print(premade1.name)

premade1.static_method()
person.static_method()
