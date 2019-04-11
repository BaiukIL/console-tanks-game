"""Wall module"""

from tanks_console_game.objects import gameobject
from tanks_console_game.configs import gameconfig


class Wall(gameobject.GameObject):
    def __init__(self, x, y, game, height, width):
        gameobject.GameObject.__init__(self, x, y, game=game,
                                       form=[[gameconfig.WALL_CHAR] * width for i in range(height)])
