from random import randrange


class Worker:
    name: str
    surname: str
    position: str
    _income: dict

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):

    def __init__(self, name: str, surname: str, position: str, income: dict):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        print(f"The full name is {self.name} {self.surname}")

    def get_total_income(self):
        print(f"Total income for {self.name} {self.surname}, {self.position} is",
              self._income["wage"] + self._income["bonus"])


test_user_1 = Position("Mark", "Polo", "designer", {"wage": randrange(100, 1000), "bonus": randrange(100, 1000)})
test_user_2 = Position("Robert", "Hemsworth", "programmer",
                       {"wage": randrange(100, 1000), "bonus": randrange(100, 1000)})
test_user_1.get_full_name()
test_user_1.get_total_income()
print()
test_user_2.get_full_name()
test_user_2.get_total_income()
