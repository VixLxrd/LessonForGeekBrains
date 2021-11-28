from random import randrange

class Car:
    speed: float
    color: str
    name: str
    is_police: bool

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def car_go(self):
        print("The car has started.")

    def car_stop(self):
        print("The car has stopped.")

    def car_turn_right(self):
        print("The car has turned right.")

    def car_turn_left(self):
        print("The car has turned left.")

    def car_show_speed(self):
        print(f"The car speed is {self.speed}")


class TownCar(Car):
    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        super().__init__(speed, color, name, is_police)

    def car_show_speed(self):
        print("This is a town car.")
        print(f"The car speed is {self.speed}")
        if self.speed > 60:
            print("The car speed is above speed limit.")


class SportCar(Car):
    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        super().__init__(speed, color, name, is_police)

    def car_show_speed(self):
        print("This is a work car.")
        print(f"The car speed is {self.speed}")
        if self.speed > 40:
            print("The car speed is above speed limit.")


class PoliceCar(Car):
    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        super().__init__(speed, color, name, is_police)


car_1 = TownCar(randrange(30, 100), "grey", "Ford", False)
car_1.car_show_speed()
print("The color is", car_1.color)
print("The name is", car_1.name)
print()
car_2 = WorkCar(randrange(30, 100), "green", "Mercedes", False)
car_2.car_show_speed()
print("The color is", car_2.color)
print("The name is", car_2.name)
print()
car_3 = SportCar(randrange(30, 100), "red", "Lamborghini", False)
print("This is a sport car.")
car_3.car_show_speed()
print("The color is", car_3.color)
print("The name is", car_3.name)
print()
car_4 = PoliceCar(randrange(30, 100), "blue", "Toyota", True)
print("This is a police car.")
car_4.car_show_speed()
print("The color is", car_4.color)
print("The name is", car_4.name)