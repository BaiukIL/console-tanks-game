"""Module of game configs. You can change them in certain range"""


# between 10 and 170
FIELD_WIDTH = 170
# between 5 and 45
FIELD_HEIGHT = 45

TANK_CHAR = '\u25A0'
BULLET_CHAR = 'o'
WALL_CHAR = '#'

BULLET_SPEED = 5


def reverse_horizontal(form):
    reversed_form = list()
    for row in form:
        reversed_form.append([char for char in reversed(row)])
    return reversed_form


def reverse_vertical(form):
    reversed_form = list()
    for row in form:
        reversed_form.insert(0, row)
    return reversed_form


TANK_RIGHT_FORM = [[TANK_CHAR, ' ', TANK_CHAR, ' ', ' '],
                   [TANK_CHAR, ' ', TANK_CHAR, ' ', TANK_CHAR],
                   [TANK_CHAR, ' ', TANK_CHAR, ' ', ' ']]
TANK_DOWN_FORM = [[TANK_CHAR, ' ', TANK_CHAR, ' ', TANK_CHAR],
                  [TANK_CHAR, ' ', TANK_CHAR, ' ', TANK_CHAR],
                  [' ', ' ', TANK_CHAR, ' ', ' ']]
TANK_LEFT_FORM = reverse_horizontal(TANK_RIGHT_FORM)
TANK_UP_FORM = reverse_vertical(TANK_DOWN_FORM)
