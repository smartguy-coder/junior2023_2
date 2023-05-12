from datetime import datetime
import winsound
import os


class Human:
    __population = 0
    # __slots__ = ['name', 'surname']

    def __init__(self, name, surname, birthday):
        self.name = name
        self.surname = surname
        self.birthday = birthday
        # self.__class__.__population += 1
        Human.__increase_population()
        with open('some.txt', 'w') as self_data_file:
            self_data_file.write(self.__str__())

    def __str__(self):
        return f'<Human> name: {self.name}, surname: {self.surname}'

    @property
    def age(self):
        my_age = (datetime.today() - self.birthday).days // 365
        return my_age

    @staticmethod
    def say_beep():
        winsound.Beep(1000, 500)

    @staticmethod
    def add_numbers(number1, number2):
        return number1 + number2

    @classmethod
    def __increase_population(cls):
        cls.__population += 1

    @classmethod
    def __decrease_population(cls):
        cls.__population -= 1

    def __del__(self):
        if os.path.exists('some.txt'):
            os.remove('some.txt')
        Human.__decrease_population()
        print('Left:', Human.__population, self)






# empty_str = str('jkhghjg')
# print(empty_str)

person1 = Human('Alex1', 'Prokopenko', datetime(1990, 5, 23))
person2 = Human('Alex525', 'Prokopenko', datetime(1990, 5, 23))
person3 = Human('Alex2525', 'Prokopenko', datetime(1990, 5, 23))
person4 = Human('Alex 2', 'Prokopenko', datetime(1990, 5, 23))

del person3
# print(person3)
person10 = Human('Alex525', 'Prokopenko', datetime(1990, 5, 23))

n = 5

print(person1.name == person4.name)
print(person1.age)
print(person1.say_beep())
print(person1.add_numbers(2, 6))
print(person1.__dict__)

person1.name = 'John'
print(person1.__dict__)

# print(Human)
# print(str)
# print(int)
#
# print(type(person1) == Human)

