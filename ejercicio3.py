class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

vector1 = Vector(10, 70)
vector2 = Vector(3.14, 4)

vector3 = vector1 + vector2
print(vector3)  

