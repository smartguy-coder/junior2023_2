from datetime import datetime


class Animal:

    def __init__(self, name, color='black'):
        self.name = f'<<{name}>>'
        self.color = color
        self.birthday = datetime.now()


cat = Animal(name='Bobik', color='Yellow')
print(cat.birthday)
