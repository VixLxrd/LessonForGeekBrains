class Stationery:
    title: str

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Drawing now!!!")


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
        self.title = title

    def draw(self):
        print(f"Drawing with a {self.title}")


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)
        self.title = title

    def draw(self):
        print(f"Drawing with a {self.title}")


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
        self.title = title

    def draw(self):
        print(f"Drawing with a {self.title}")


draw_1 = Pen("pen")
draw_1.draw()
draw_2 = Pencil("pencil")
draw_2.draw()
draw_3 = Handle("handle")
draw_3.draw()
