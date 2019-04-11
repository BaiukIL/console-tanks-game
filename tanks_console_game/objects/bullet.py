"""Bullet module"""

from tanks_console_game.objects import gameobject
from tanks_console_game.configs import gameconfig, gamename
from tanks_console_game.properties import weapon


class Bullet(gameobject.MoveObject, weapon.Weapon):
    def __init__(self, x, y, game, direction, damage, speed_value=gameconfig.BULLET_SPEED):
        gameobject.MoveObject.__init__(self, x, y, form=[[gameconfig.BULLET_CHAR]], game=game,
                                       direction=direction, speed_value=speed_value)
        weapon.Weapon.__init__(self, damage)
        try:
            self._fix_collisions(None)
        except gameobject.CollisionOccurred:
            pass

    def move(self, act=None):
        gameobject.MoveObject.move(self, self.speed.direction)

    def hit(self, obj):
        # if object has health attribute
        if obj in self.groups[gamename.HEALTH_OBJECTS]:
            obj.decrease_health(self.damage)

    def _action_after_collision(self, obj):
        self.hit(obj)
        self._delete()
