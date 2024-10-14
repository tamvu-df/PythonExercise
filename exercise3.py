class Shape:
    def area(self) -> float:
        pass
    def circumference(self) -> float:
        pass

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius
    def area(self) -> float:
        return 3.14 * self.radius**2 
    def circumference(self) -> float:
        return 3.14 * self.radius * 2
    
class Square(Shape):
    def __init__(self, side: float):
        self.side = side
    def area(self) -> float:
        return self.side ** 2
    def circumference(self) -> float:
        return self.side * 4

class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width
    def area(self) -> float:
        return self.length * self.width
    def circumference(self) -> float:
        return (self.length + self.width) * 2
if __name__ == "__main__":
    circle = Circle(5)
    square = Square(4)
    rectangle = Rectangle(3, 5)
    print(f"Circle area: {circle.area()}")
    print(f"Circle circumference: {circle.circumference()}")
    print(f"Square area: {square.area()}")
    print(f"Square circumference: {square.circumference()}")
    print(f"Rectangle area: {rectangle.area()}")
    print(f"Rectangle circumference: {rectangle.circumference()}")