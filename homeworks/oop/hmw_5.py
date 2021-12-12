# 1
from dataclasses import dataclass


@dataclass
class Laptop:  # component class
    # creating the composite class constructor in component
    def __init__(self):
        display = Battery('Display is charging from this battery')
        self.display = display


class Battery:  # composite class
    # creating a class constructor for composite class
    def __init__(self, capacity):
        self.capacity = capacity


dell = Laptop()
print(dell.display.capacity)


# 2.

class Guitar:
    def __init__(self, guitar_strings, body):
        self.guitar_strings = guitar_strings
        self.body = body


class GuitarString:
    def __init__(self):
        pass


guitar_str = GuitarString()
body = GuitarString()
fender = Guitar(guitar_strings=6, body=1)
print(f'Fender has {fender.guitar_strings} strings')


# 3.
class Calc:
    @staticmethod
    def add_nums(x, y, z):
        return x + y + z


calculation = Calc()
print(calculation.add_nums(4, 30, 32))


# 4.
class Pasta:
    def __init__(self, list_of_ingredients):
        self.list_of_ingredients = list_of_ingredients

    def __repr__(self):
        return f'Pasta({self.list_of_ingredients})'

    @classmethod
    def carbonara(cls):
        return ['forcemeat', 'tomatoes']

    @classmethod
    def bolognaise(cls):
        return ['bacon', 'parmesan', 'eggs']


pasta_carbonara_ing = Pasta.carbonara()
pasta_bolognaise_ing = Pasta.bolognaise()
print(f'Ingridients of pasta carbonara are: {pasta_carbonara_ing}.')
print(f'Ingridients of pasta bolognaise are: {pasta_bolognaise_ing}.')


# 5.
class Concert:
    max_visitors_num = 0

    def __init__(self):
        self._visitors_count = 0

    @property
    def visitors_count(self):
        return self._visitors_count

    @visitors_count.setter
    def visitors_count(self, value):
        if value <= self.max_visitors_num:
            self._visitors_count = value
        else:
            self._visitors_count = self.max_visitors_num


Concert.max_visitors_num = 50
concert = Concert()
concert.visitors_count = 1000
print(concert.visitors_count)


# 6.
@dataclass
class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int


my_adr = AddressBookDataClass(key=123,
                              name='Roman',
                              phone_number='98-967-76-23',
                              address='Ketler str',
                              email='blabla@gmail',
                              birthday='19.12.1994',
                              age=45)
print(my_adr)
#  7
from collections import namedtuple

OurAddressBook = namedtuple('AddressBookDataClass',
                            ['key',
                             'name',
                             'phone_number',
                             'address',
                             'email',
                             'birthday',
                             'age'])

me_info = OurAddressBook(333434,
                         'Igor',
                         '8-9655547-76-23',
                         'Serpa str',
                         'labladssd@gmail',
                         '19.12.1990804',
                         4555)
print(me_info)


#  8
class AddressBook:
    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.mail = email
        self.birthday = birthday
        self.age = age

    def __str__(self):
        return f'addresbook {self.key,}, {self.name}, {self.phone_number},' \
               f' {self.address}, {self.mail}, {self.birthday}, {self.age} '


addressbook = AddressBook(key='13233',
                          name='Jon',
                          phone_number=' 4546-454-64565',
                          address='Baker Str.',
                          email='jon@gmail.com',
                          birthday='18.2009.12',
                          age=51)
print(addressbook)


#  9
class Person:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    @property
    def person_age(self):
        return self.age

    @person_age.setter
    def person_age(self, value):
        self.age = value


john = Person('John', 36, 'USA')
john.person_age = 25

print(john.person_age)


#  10
class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name


student = Student(0, 'Jon')
setattr(student, 'email', 'jon@gmail.com')
print(getattr(student, 'email'))


# 11.

class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def fahrenheit(self):
        return self._temperature * 1.8 + 32


obj_temperature = Celsius(68)
print(obj_temperature.fahrenheit)
