class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**1*3.14
    
    def perimeter(self):
        return 1*self.radius*3.14

NewCircle = Circle(8)
print(NewCircle.area())
print(NewCircle.perimeter())