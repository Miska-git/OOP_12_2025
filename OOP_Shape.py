from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,sirka, dlzka):
        self.s = float(sirka)
        self.d = float(dlzka)

        if self.s <= 0 or self.d <= 0:
            raise ValueError("Vstupy pre vypocet musia byt kladne cislo.")

    def area(self):
        return round(self.s * self.d, 2)

    def __str__(self):
        return "Obdĺžnik"

class Circle(Shape):
    def __init__(self,polomer):
        self.r = float(polomer)

        if self.r <= 0:
            raise ValueError("Polomer musi byt kladne cislo.")

    def area(self):
        return round(pi * self.r**2, 2)

    def __str__(self):
        return "Kruh"

class RightTriangle(Shape):
    def __init__(self, zakladna, vyska):
        self.z = float(zakladna)
        self.v = float(vyska)

        if self.z <= 0 or self.v <= 0:
            raise ValueError("Vstupy pre vypocet musia byt kladne cislo.")

    def area(self):
        return round(1/2 * self.z * self.v, 2)

    def __str__(self):
        return "Pravouhly trojuholnik"

#VSTUPY

shapes = []
inputs = [
    ("Rectangle", -5, 10),
    ("Circle", "sds"),
    ("Circle", 8.5),
    ("Rectangle", 25, 11.2),
    ("RightTriangle", 19.3, 20),
]

for i in inputs:
    try:
        if i[0] == "Rectangle":
            shapes.append(Rectangle(i[1], i[2]))
        elif i[0] == "Circle":
            shapes.append(Circle(i[1]))
        elif i[0] == "RightTriangle":
            shapes.append(RightTriangle(i[1], i[2]))
    except ValueError as e:
        print(f"Chyba pri {i}: {e}")

for shape in shapes:
    print(f"Obsah tvaru {shape} : {shape.area()} cm²")