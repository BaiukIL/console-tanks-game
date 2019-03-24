"""Tank module"""


import gameobject_
import gamenames_
import gameconfig_
import unit_
import bullet_


class Tank(gameobject_.MoveObject, unit_.Unit):
    # this immutable array contains configurations of orientations and is identical for all members
    # it's efficient to make it static in order to avoid memory problems
    orientations = {gamenames_.RIGHT: gameconfig_.TANK_RIGHT_FORM,
                    gamenames_.LEFT: gameconfig_.TANK_LEFT_FORM,
                    gamenames_.DOWN: gameconfig_.TANK_DOWN_FORM,
                    gamenames_.UP: gameconfig_.TANK_UP_FORM}

    def __init__(self, x, y, game, health, damage, speed_value, start_direction=gamenames_.RIGHT):
        gameobject_.MoveObject.__init__(self, x, y,
                                        form=Tank.orientations[start_direction],
                                        direction=start_direction,
                                        speed_value=speed_value,
                                        game=game)
        unit_.Unit.__init__(self, health=health, damage=damage)
        self.game_reference = game
        self.add_to_group(gamenames_.HEALTH_OBJECTS)

    def action(self):
        self.shoot()

    def shoot(self):
        if self.speed.direction is gamenames_.RIGHT:
            bullet_x = self.right_border + 1
            bullet_y = (self.up_border + self.down_border) // 2
        elif self.speed.direction is gamenames_.LEFT:
            bullet_x = self.left_border - 1
            bullet_y = (self.up_border + self.down_border) // 2
        elif self.speed.direction is gamenames_.UP:
            bullet_x = (self.left_border + self.right_border) // 2
            bullet_y = self.up_border - 1
        elif self.speed.direction is gamenames_.DOWN:
            bullet_x = (self.left_border + self.right_border) // 2
            bullet_y = self.down_border + 1
        else:
            raise Exception(self.speed.direction, "- incorrect direction")
        bullet_.Bullet(bullet_x, bullet_y, damage=self.damage, direction=self.speed.direction, game=self.game_reference)

    def rotate_form(self, direction):
        self.form = Tank.orientations[direction]

    def die(self):
        self.__del__()
