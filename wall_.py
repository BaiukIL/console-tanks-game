"""Wall module"""


import gameobject_
import gameconfig_


class Wall(gameobject_.GameObject):
    def __init__(self, x, y, game, height, width):
        gameobject_.GameObject.__init__(self, x, y, game=game,
                                        form=[[gameconfig_.WALL_CHAR] * width for i in range(height)])
