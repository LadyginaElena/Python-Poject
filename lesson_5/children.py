from parents import Parents

class Children(Parents):
    def __init__(self, name, age, character, eyes='Blue'):
        super().__init__(name, age, character)
        self.eyes = eyes

    def laugh(self):
        print(f'{self.name} laughs contagiously')

    def print_info(self):
        print(f"{self.name} cooked cakes")