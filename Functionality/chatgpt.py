
'''
Question 3:
Implement a Python class called Rectangle with methods to calculate its area and perimeter.
'''
class Rectangle(object):
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        area = self.l * self.w
        return area


newrec = Rectangle(5, 3)
print(newrec.area())


