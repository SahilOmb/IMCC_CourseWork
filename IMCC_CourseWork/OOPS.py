
class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

  
    def get_area(self):
        
        area = self.length * self.width
        return area



my_rect = Rectangle(5, 10)

total_area = my_rect.get_area()

print("The area of the rectangle is:", total_area)
