class Human:
    def __init__(self, firstname: str,last_name: str,
                        age: int,birth_place: str,addresses=None):
        if addresses is None:
            addresses = []

        self.addresses = addresses
        self.firstname = firstname
        self.last_name = last_name
        self.age = age
        self.birth_place = birth_place

    def add_address(self,address:str):
        self.addresses.append(address)


human_1 = Human(firstname="nugo",last_name="svianadze",age=21,birth_place="gori")
print(human_1.last_name)
Human.add_address(human_1,"gori")
human_1.add_address("tbilis")
print(human_1.addresses)