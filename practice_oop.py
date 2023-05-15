# game
from abc import ABC, abstractmethod
from enum import Enum
import random
import winsound


class CONFIG(Enum):
    MAX_LIFE = 100
    TANK_POWER = 50
    TANK_PRECISION = 50
    ARTILLERY_POWER = 80
    ARTILLERY_PRECISION = 30


class Character(ABC):

    def __init__(self, weapon_type, number, load, has_thermal_imager_equipment=False):
        self.type = weapon_type
        self.number = number
        self.load = load
        self.has_thermal_imager_equipment = has_thermal_imager_equipment
        self.life = CONFIG.MAX_LIFE.value
        self.documentation = 'bla-bla'

    @abstractmethod
    def attack(self, other):
        pass

    def get_aid(self, points):
        self.life += points
        if self.life > CONFIG.MAX_LIFE.value:
            self.life = CONFIG.MAX_LIFE.value

    def __str__(self):
        return f'{self.type} #{self.number} ({self.life} points of life)'

    @property
    def is_alive(self):
        return self.life > 0


class Tank(Character):
    def __init__(self, number, color, load,  has_thermal_imager_equipment=True):
        super().__init__(weapon_type='Tank', number=number, load=load, has_thermal_imager_equipment=has_thermal_imager_equipment)
        self.color = color
        self.power = CONFIG.TANK_POWER.value
        self.precision = CONFIG.TANK_PRECISION.value
        del self.documentation
        if self.has_thermal_imager_equipment:
            self.precision += 10

    def attack(self, other: Character):
        if not self.is_alive:
            print('I am dead')
            return

        if not self.load:
            print('NO WEAPON')
            return

        self.load -= 1
        print(self, '>>>')
        print('Reload...\nFire!!!!')
        # winsound.Beep(500, 500)
        in_point = random.randint(1, 101)

        if in_point <= self.precision:
            other.life -= self.power
            if other.life < 1:
                other.life = 0
            print(f'I hit {other}')
        else:
            print('Missed')


class Artillery(Character):
    def __init__(self, number, weight, load):
        super().__init__(number=number, load=load, weapon_type='Arta')
        self.weight = weight
        self.power = CONFIG.ARTILLERY_POWER.value
        self.precision = CONFIG.ARTILLERY_PRECISION.value
        if self.has_thermal_imager_equipment:
            self.precision += 70

    def attack(self, other: Character):
        print(self, '>>>')
        if self.load:
            self.load -= 1
            in_point = random.randint(1, 80)

            if in_point <= self.precision:
                other.life -= self.power
                print(f'I hit {other}')
            else:
                print('Missed, but artillery is the best')
        else:
            print('NO WEAPON')


t64_1 = Tank(555, 'black', 10, has_thermal_imager_equipment=True)
arta = Artillery(1025, weight=500.2, load=50)
# print(t64_1.life)
t64_1.attack(arta)
arta.get_aid(23)
t64_1.attack(arta)
arta.attack(t64_1)
arta.attack(t64_1)
arta.attack(t64_1)
arta.attack(t64_1)
arta.attack(t64_1)
arta.attack(t64_1)
arta.attack(t64_1)
t64_1.attack(arta)
t64_1.attack(arta)
t64_1.attack(arta)
t64_1.attack(arta)
t64_1.attack(arta)
print(arta.is_alive)

t64_1.info = 'gggggggggggg'

print(t64_1.__dict__)



pass
