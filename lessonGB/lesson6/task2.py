class Road:
    _length: int
    _width: int

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def func(self, weight, depth):
        print(self.length * self.width * weight * depth / 1000, "ton", sep=" ")


road = Road(20, 5000)
weight_user = int(input("Weight: "))
depth_user = int(input("Depth: "))
road.func(weight_user, depth_user)
