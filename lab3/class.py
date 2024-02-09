
#ex1
class Strings:
    def __init__(self):
        self.string = input()
    
    def pr(self):
        string_s = self.string.upper()
        print(string_s)

strings = Strings()
strings.pr()

#ex2

class Shape():
    def __init__(self):
        pass

    def area(self):
        return 0
    
class Square(Shape):

    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length * self.length
    
square = Square()
print(square.area())

#ex3

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self, x, y):
        self.x = x
        self.y = y

    def dist(self, second_x, second_y):
        return (((self.x - second_x) ** 2) + ((self.y - second_y) ** 2)) ** (1 / 2)

