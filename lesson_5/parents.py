class Parents:

    hair = "brunet"

    def __init__(self, name="Parents_1", age=0, character="character"):
        self.name = name
        self.age = age
        self.character = character

    def print_info(self):
        print(f"{self.name} печет пироги")
