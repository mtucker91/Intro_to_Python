# Type code for Rectangle class here
class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def rectangle_area(self):
        area = self.length * self.width
        print(f'The area of the rectangle is {area}')

if __name__ == "__main__":
    # Type main section of code here
    print('Rectangle calculations using class')
    rect_len = int(input(f'Input the length:\n'))
    rect_wid = int(input(f'Input the width:\n'))
    my_rect = Rectangle(rect_len, rect_wid)
    my_rect.rectangle_area()