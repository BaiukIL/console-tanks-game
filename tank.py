"""Tank module"""


import gameobject
import gamenames
import gameconfig
import unit
import bullet


class Tank(gameobject.MoveObject, unit.Unit):
    # this immutable array contains configurations of orientations and is identical for all members
    # it's efficient to make it static in order to avoid memory problems
    orientations = {gamenames.RIGHT: gameconfig.TANK_RIGHT_FORM,
                    gamenames.LEFT: gameconfig.TANK_LEFT_FORM,
                    gamenames.DOWN: gameconfig.TANK_DOWN_FORM,
                    gamenames.UP: gameconfig.TANK_UP_FORM}

    def __init__(self, x, y, game, health, damage, speed_value, start_direction=gamenames.RIGHT):
        gameobject.MoveObject.__init__(self, x, y,
                                       form=Tank.orientations[start_direction],
                                       direction=start_direction,
                                       speed_value=speed_value,
                                       game=game)
        unit.Unit.__init__(self, health=health, damage=damage)
        self.game_reference = game
        self._add_to_group(gamenames.HEALTH_OBJECTS)

    def action(self):
        self.shoot()

    def shoot(self):
        if self.speed.direction is gamenames.RIGHT:
            bullet_x = self.right_border + 1
            bullet_y = (self.up_border + self.down_border) // 2
        elif self.speed.direction is gamenames.LEFT:
            bullet_x = self.left_border - 1
            bullet_y = (self.up_border + self.down_border) // 2
        elif self.speed.direction is gamenames.UP:
            bullet_x = (self.left_border + self.right_border) // 2
            bullet_y = self.up_border - 1
        elif self.speed.direction is gamenames.DOWN:
            bullet_x = (self.left_border + self.right_border) // 2
            bullet_y = self.down_border + 1
        else:
            raise Exception(self.speed.direction, "- incorrect direction")
        bullet.Bullet(bullet_x, bullet_y, damage=self.damage, direction=self.speed.direction, game=self.game_reference)

    def _rotate_form(self, direction):
        self.form = Tank.orientations[direction]

    def _die(self):
        self._delete()
