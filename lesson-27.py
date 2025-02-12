# დავწეროთ ფუნქცია რომელიც ლისტიდან ითვლის
# საშუალოს მაგრამ გამოიწვიოს ერორი თუ რომელიღაც
# რიცხვი არ არის ან ლისტი ცარიელია


# def average(numbers: list) -> float:
#     if len(numbers) < 1:
#         raise ValueError("List cant be empty!")
#
#     for num in numbers:
#         if not isinstance(num, int) and not isinstance(num, float):
#             raise ValueError("List elements must be int/float!!")
#
#     return sum(numbers) / len(numbers)
#
#
# try:
#     num = int(input("num : "))
#     print(average([num]))
#     # print(average([]))
# except ValueError as e:
#     print(e)

# print(type("asdsad"), int(), str)

class Human:
    IS_HOMO_SAPIENS = True
    TYPE = "Homo Sapiens"

    def __init__(self, first_name: str, last_name: str,
                 age: int, birth_place: str, addresses=None):
        if addresses is None:
            addresses = []

        self.addresses = addresses
        self.first_name = first_name
        self.last_name = last_name
        self._age = age
        self.__birth_place = birth_place

    def __str__(self):
        return f"{self.first_name} - {self.last_name} - {self.get_birth_place}"

    def add_address(self, address: str):
        self.addresses.append(address)

    @property
    def get_birth_place(self):
        return self.__birth_place

    @property
    def name(self):
        return self.first_name

    @name.setter
    def name(self, name):
        self.first_name = name

    def set_first_name(self, name):
        self.first_name = name

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    @staticmethod
    def get_human_type():
        return Human.TYPE

    @classmethod
    def get_human_type_with_class_method(cls):
        return cls.TYPE


human_1 = Human("nugo", "svianadze",
                21, "Gori")
human_2 = Human("giorgi", "giorgadze",
                25, "Tbilisi")
human_3 = Human("Demo", "Demo",
                30, "Kareli")

human_instances = [human_1, human_2, human_3]

for human in human_instances:
    print(human)

# del human_2.first_name

# print(human_1._age)

# print(human_1.get_birth_place)
# print(human_1.name)
# human_1.name = "Nugzari"
# print(human_1.name)
# print(human_1.get_full_name)
#
# print("~~~~")
# print(Human.get_human_type(human_1))
# print(Human.get_human_type_with_class_method())
# print("~~~~")
#
# # human_1.set_first_name("Nugzari")
#
# print()
# print(human_1.addresses)
# human_1.add_address("Tbilisi")
# Human.add_address(human_1, "Gori")
# print(human_1.addresses)

# print(human_1.IS_HOMO_SAPIENS)
# print(Human.IS_HOMO_SAPIENS)