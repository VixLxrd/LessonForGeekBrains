from abc import ABC, abstractmethod


class AbsGarments(ABC):
    @abstractmethod
    def coat_cloth(self):
        pass

    @abstractmethod
    def suit_cloth(self):
        pass

    @abstractmethod
    def total_cloth(self):
        pass


class Garments(AbsGarments):
    def __init__(self, size: int, height: int):
        self.size = size
        self.height = height

    @property
    def coat_cloth(self):
        return round(self.size / 6.5 + 0.5, 1)

    @property
    def suit_cloth(self):
        return round(self.size * 2 + 0.3, 1)

    @property
    def total_cloth(self):
        return round(self.size / 6.5 + 0.5, 1) + round(self.size * 2 + 0.3, 1)


my_clothes = Garments(50, 200)
print(my_clothes.coat_cloth)
print(my_clothes.suit_cloth)
print(my_clothes.total_cloth)
