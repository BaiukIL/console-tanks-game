"""Bullet module"""


import gameobject_
import gamenames_
import gameconfig_
import weapon_


class Bullet(gameobject_.MoveObject, weapon_.Weapon):
    def __init__(self, x, y, game, direction, damage, speed_value=gameconfig_.BULLET_SPEED):
        gameobject_.MoveObject.__init__(self, x, y, form=[[gameconfig_.BULLET_CHAR]], game=game,
                                        direction=direction, speed_value=speed_value)
        weapon_.Weapon.__init__(self, damage)
        self.fix_collisions(None)

    def move(self, act=None):
        gameobject_.MoveObject.move(self, self.speed.direction)

    def action_after_collision(self, obj):
        self.hit(obj)
        self.__del__()

    def hit(self, obj):
        # if object has health attribute
        if obj in self.groups[gamenames_.HEALTH_OBJECTS]:
            obj.decrease_health(self.damage)
