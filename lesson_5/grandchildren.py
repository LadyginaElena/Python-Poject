from parents import Parents
from children import Children


class Grandchildren(Children, Parents):
    def __init__(self, name, age, character, eyes, language):
        super().__init__(name, age, character, eyes)
        self.__language = language

    def walk(self):
        return f'I am walking'

    def print_info(self):
        print(f"{self.name} eat pies and cakes")

    def get_language(self):
        return self.__language if self.__language else None

    def set_language(self, language):
        self.__language = language
        self.hair = 'Blonde'