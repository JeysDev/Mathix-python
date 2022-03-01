import math
class Vector2():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return (f'({self.x}, {self.y})')

    def Add(self, vec2):
        self.x += vec2.x
        self.y += vec2.y
    def Substract(self, vec2):
        self.x -= vec2.x
        self.y -= vec2.y
    def Multiply(self, vec2):
        self.x *= vec2.x
        self.y *= vec2.y
    def Divide(self, vec2):
        self.x /= vec2.x
        self.y /= vec2.y
    
    def Add(vec1, vec2):
        return Vector2(vec1.x + vec2.x, vec1.y + vec2.y)        
    def Substract(vec1, vec2):
        return Vector2(vec1.x - vec2.x, vec1.y - vec2.y)
    def Multiply(vec1, vec2):
        return Vector2(vec1.x * vec2.x, vec1.y * vec2.y)
    def Divide(vec1, vec2):
        return Vector2(vec1.x / vec2.x, vec1.y / vec2.y)

    def Lenght(self):
        return math.sqrt(self.x * self.x, self.y * self.y)



sample = Vector2(-3, 6)
print(sample)
sample.Divide(Vector2(1, 4))
print(sample)
bsample = Vector2(1,0)
bsample.Multiply(Vector2(2,6))
print(bsample)
print(Vector2.Add(sample, bsample))
print(Vector2.Divide(bsample, sample))
print(sample.Lenght())