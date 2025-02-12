from abc import ABC, abstractmethod
"""
მშობელი კლასი: ElectronicDevice
ველები: brand (ბრენდი), power_usage (მოხმარებული ენერგია ვატებში),
battery_life (ბატარეის ხანგრძლივობა საათებში)
@property: info – აბრუნებს ტექსტს, რომელიც აღწერს მოწყობილობას.
@staticmethod: is_energy_efficient(power_usage) – აბრუნებს True-ს, თუ
მოწყობილობის მოხმარებული ენერგია 50W-ზე ნაკლებია, წინააღმდეგ შემთხვევაში False.
@classmethod: from_string(cls, data) – იღებს ტექსტურ მონაცემს (მაგალითად, "Laptop,Dell,65,8,16")
და აბრუნებს შესაბამისი კლასის ობიექტს.
შვილობილი კლასები:
Laptop კლასი

დამატებითი ველი: ram (ოპერატიული მეხსიერება, GB)
გადაწერილი info მეთოდი, რომელიც მოიცავს RAM-ის დეტალებს.

Smartphone კლასი

დამატებითი ველი: camera_megapixels (კამერის ხარისხი MP-ში)
გადაწერილი info მეთოდი, რომელიც მოიცავს კამერის დეტალებს.

"""


class ElectronicDevice:
    def __init__(self, brand: str, power_usage: int, battery_life: int):
        self.brand = brand
        self.power_usage = power_usage
        self.battery_life = battery_life

    @property
    def info(self) -> str:
        return (f"brand : {self.brand}, power usage in wats : {self.power_usage}  "
                f"battery life : {self.battery_life}")

    @staticmethod
    def is_energy_efficient(power_usage: int) -> bool:
        return True if power_usage < 50 else False

    @classmethod
    def from_string(cls, data: str):
        brand, power_usage, battery_life = data.split(",")
        return cls(brand, int(power_usage), int(battery_life))


class Laptop(ElectronicDevice):
    def __init__(self, brand: str, power_usage: int, battery_life: int, ram: int):
        super().__init__(brand, power_usage, battery_life)
        self.ram = ram

    @property
    def info(self) -> str:
        return f"{super().info} , Ram : {self.ram}"

    @classmethod
    def from_string(cls, data: str):
        brand, power_usage, battery_life, ram = data.split(",")
        return cls(brand, int(power_usage), int(battery_life), int(ram))


class SmartPhone(ElectronicDevice):
    def __init__(self, brand: str, power_usage: int, battery_life: int, camera_megapixel: int):
        super().__init__(brand, power_usage, battery_life)
        self.camera_megapixel = camera_megapixel

    @property
    def info(self) -> str:
        return f"{super().info} , Camera MegaPixel : {self.camera_megapixel}"

    @classmethod
    def from_string(cls, data: str):
        brand, power_usage, battery_life, camera_mp = data.split(",")
        return cls(brand, int(power_usage), int(battery_life), int(camera_mp))


macbook = Laptop("Apple", 45, 12, 16)
touchpad = Laptop("Lenovo", 65, 8, 8)
acer = Laptop.from_string("Acer,50,10,16")

xiaomi = SmartPhone("Xiaomi", 40, 12, 16)
iphone = SmartPhone("Apple", 35, 6, 16)
google_px = SmartPhone.from_string("Google,45,16,32")

# print(macbook.info)
# print(acer.info)
# print(touchpad.info)
#
# print(xiaomi.info)
# print(iphone.info)
# print(google_px.info)
# print(ElectronicDevice.is_energy_efficient(65))

# polymorphism


class Animal:
    pass


#
# print(dog.sound())
# print(cat.sound())


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other_self):
        print("__add__ method :", self, "--", other_self)
        return Vector(self.x + other_self.x, self.y + other_self.y)

    def __str__(self):
        return f"{self.x} , {self.y}"


# vector_1 = Vector(1, 2)
# vector_2 = Vector(3, 4)
# vector_3 = Vector(5, 6)
# vector_4 = vector_1 + vector_2 + vector_3
#
# print(f"vector_4 : {vector_4}")


class Dog:
    def sound(self):
        return "Waf!!"


class Cat:
    def sound(self):
        return "Meouw!!!"


def make_animal_sound(obj):
    print(type(obj))
    return obj.sound()


# for obj in [Dog(), Cat()]:
#     print(make_animal_sound(obj))


class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def can_move(self):
        return True


class Car(Vehicle):
    def start(self):
        return "car engine started"

    def stop(self):
        return "car engine stopped"

# vehicle = Vehicle()
# print(vehicle)

#
# car = Car()
# print(car.start())


class Animal(ABC):
    def __init__(self, name, specie):
        self.name = name
        self.specie = specie

    @abstractmethod
    def make_noice(self):
        pass


class Bird(Animal):
    def make_noice(self):
        return "GUGU!"

    @property
    def can_fly(self):
        return True


class Dog(Animal):
    def make_noice(self):
        return "Waf Waf!"

    @property
    def can_running(self):
        return True


bird = Bird("Test", "Mercxali")
print(bird.make_noice())
print(bird.can_fly)

dog = Dog("Jeka", "PitBull")
print(dog.make_noice())
print(dog.can_running)
