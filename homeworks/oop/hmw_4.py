# 1. Create a Vehicle class with max_speed and mileage instance attributes

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


my_vehicle = Vehicle(220, 25)
print(f'My vehicle maximum speed is {my_vehicle.max_speed} and my vehicle mileage is {my_vehicle.mileage}')


# 2. Create a child class Bus that will inherit all the variables and methods of the Vehicle class and will have seating_capacity own method

class Bus(Vehicle):
    def __init__(self, max_speed, mileage, seating_capacity):
        super().__init__(max_speed, mileage)
        self.seating_capacity = seating_capacity

    def seat_info(self):
        print(f'Bus seating capacity is {self.seating_capacity} people')


holiday_bus = Bus(459, 56, 98)

# 3. Determine which class a given Bus object belongs to (Check type of an object)

print(type(holiday_bus))

# 4. Determine which class a named school_bus and determine if school_bus is also an instance of the Vehicle class

print(isinstance(holiday_bus, Vehicle))


# 5. Create a new class School with get_school_id and number_of_students instance attributes

class School:
    def __init__(self, get_school_id, number_of_students):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students


my_school = School("Jon Wick", 345)

print(f'My school ID is {my_school.get_school_id} and school capacity is {my_school.number_of_students} students')


# 6*. Create a new class SchoolBus that will inherit all the methods from School and Bus and will have its own - bus_school_color

class SchoolBus(School, Bus):
    def __init__(self, max_speed, mileage, seating_capacity, bus_school_color):
        super().__init__(max_speed, mileage, seating_capacity)
        self.bus_school_color = bus_school_color

    def bus_color(self):
        print(f'Bus color is {self.bus_school_color}.')


#  7. Polymorphism: Create two classes: Bear, Wolf. Both of them should have make_sound method. Create two instances, one of Bear and one of Wolf,
# make a tuple of it and by using for call their action using the same method.

class Bear:
    def __init__(self, sound):
        self.sound = sound

    def make_sound(self):
        return f'Bear make sound {self.sound}!'


class Wolf:
    def __init__(self, sound):
        self.sound = sound

    def make_sound(self):
        return f'Wolf make sound {self.sound}!'


beear = Bear('hr!')
woolf = Wolf('au!')
animals = (beear, woolf)

for animal_sound in animals:
    print(animal_sound.make_sound())


# # 8*. Create class City with name, population instance attributes, return a new instance only when population > 1500,
# # otherwise return message: "Your city is too small". Hint: use magic methods / patterns
# class City:
#     def __init__(self, name, population):
#         self.name = name
#         self.population = population
#
#     def check_population(self):
#         if self.population > 1500:
#             return self.population
#         else:
#             return f'Your city {self.name} is too small'
#
#
# Toronto = City('Toronto', 50000)
# Male = City('Male', 1000)
# all_cities = (Toronto, Male)
#
# for i in all_cities:
#     print(i.check_population())
