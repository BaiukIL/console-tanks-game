"""This module contains strategies of game's bots (i. e. player_.Bot objects).
Strategy can be added by Bot.set_strategy function. There's is one: square_path. Bot of this strategy goes
in square's shape and shoot after rotation
You can write your own strategy and Bots will be cleverer!"""


def square_path(side):
    while True:
        yield ' '
        for i in range(side):
            yield 'w'
        yield ' '
        for i in range(side):
            yield 'a'
        yield ' '
        for i in range(side):
            yield 's'
        yield ' '
        for i in range(side):
            yield 'd'
