class Cell:
    def __init__(self, cell_unit_count: int):
        self.cell_unit_count = cell_unit_count

    def __str__(self):
        return f"It consists of {self.cell_unit_count} units."

    def __add__(self, other):
        return Cell(self.cell_unit_count + other.cell_unit_count)

    def __sub__(self, other):
        if self.cell_unit_count > other.cell_unit_count:
            return Cell(self.cell_unit_count - other.cell_unit_count)
        else:
            print("Illegal operation")

    def __mul__(self, other):
        return Cell(self.cell_unit_count * other.cell_unit_count)

    def __truediv__(self, other):
        return Cell(self.cell_unit_count // other.cell_unit_count)

    def make_order(self, units_per_row: int):
        row = ''
        full_rows = self.cell_unit_count // units_per_row
        incomplete_row = self.cell_unit_count % units_per_row

        for i in range(full_rows):
            row += "*" * units_per_row + '\\n'

        row += "*" * incomplete_row
        return row


cell1 = Cell(10)
cell2 = Cell(3)
print("This is cell 1: ", cell1)
print("This is cell 2: ", cell2)
print("This is cell 1 + cell2: ", cell1 + cell2)
print("This is cell 1 - cell2: ", cell1 - cell2)
print("This is cell 1 x cell2: ", cell1 * cell2)
print("This is cell 1 / cell2: ", cell1 / cell2)
print("Testing the make.order method: ")
print(Cell(24))
print(Cell(24).make_order(5))
