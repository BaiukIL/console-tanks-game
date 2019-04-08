"""Field module"""


from os import system
import gamenames


def clear_scr():
    system('clear')


class Field:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.left_border = 0
        self.right_border = width - 1
        self.up_border = 0
        self.down_border = height - 1
        self.buffer = [[gamenames.EMPTY_CHAR] * height for i in range(width)]

    def draw_object(self, obj):
        start_x, start_y, form = obj.get_data()
        y = start_y
        for string in form:
            x = start_x
            for char in string:
                self.buffer[x][y] = char
                x += 1
            y += 1

    def update(self):
        clear_scr()
        self.print_field()
        self.clear_buffer()

    def clear_buffer(self):
        self.buffer = [[gamenames.EMPTY_CHAR] * self.height for i in range(self.width)]

    def print_field(self):
        for y in range(self.height):
            for x in range(self.width):
                print(self.buffer[x][y], end='')
            print()
