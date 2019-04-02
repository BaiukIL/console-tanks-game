"""Basic object module (game objects are inherited from this one)"""


import gamenames_
import vector_


class GameObject:
    def __init__(self, x, y, form, game):
        self.x = x
        self.y = y
        # form is coordinate representation of an object. Game objects represents as strings and field as columns
        self.form = form
        # reference to all game's objects. Using to avoid collisions with other objects
        self.classes = game.classes
        self._add_to_classes()
        self.groups = game.groups

    def _delete(self):
        for cls in self.classes.values():
            if self in cls:
                cls.remove(self)
        for group in self.groups.values():
            if self in group:
                group.remove(self)

    @property
    def height(self):
        return len(self.form)

    @property
    def width(self):
        return len(self.form[0])

    @property
    def left_border(self):
        return self.x

    @property
    def right_border(self):
        return self.x + self.width - 1

    @property
    def up_border(self):
        return self.y

    @property
    def down_border(self):
        return self.y + self.height - 1

    def _add_to_classes(self):
        if self not in self.classes[type(self)]:
            self.classes[type(self)].append(self)

    def _add_to_group(self, group_name):
        if self not in self.groups[group_name]:
            self.groups[group_name].append(self)

    def get_data(self):
        return self.x, self.y, self.form


class MoveObject(GameObject):
    def __init__(self, x, y, game, form, direction, speed_value):
        super().__init__(x, y, game=game, form=form)
        self.speed = vector_.Vector(direction=direction, value=speed_value)
        self._add_to_group(gamenames_.MOVE_OBJECTS)

    def move(self, direction):
        for step in range(self.speed.value):
            # if collision occurred basic_movement returns StopIteration
            try:
                self._basic_movement(direction)
            except StopIteration:
                break

    def _basic_movement(self, direction):
        self.speed.direction = direction
        self._rotate_form(direction)
        if direction == gamenames_.UP:
            self.y -= 1
        elif direction == gamenames_.DOWN:
            self.y += 1
        elif direction == gamenames_.LEFT:
            self.x -= 1
        elif direction == gamenames_.RIGHT:
            self.x += 1
        else:
            raise Exception(self.speed.direction, "- incorrect direction")

        collision_occurred = self._fix_collisions(direction)
        if collision_occurred:
            raise StopIteration

    # if collision occurred it returns true, else - false
    def _fix_collisions(self, direction):
        collision_occurred = False
        for obj in self._objects_array():
            if obj is not self and self._in_collision_with(obj):
                collision_occurred = True
                self._fix_collision(obj, direction)
                self._action_after_collision(obj)
        return collision_occurred

    def _fix_collision(self, obj, direction):
        if direction == gamenames_.UP:
            self.y += abs(obj.down_border - self.up_border) + 1
        elif direction == gamenames_.DOWN:
            self.y -= abs(self.down_border - obj.up_border) + 1
        elif direction == gamenames_.LEFT:
            self.x += abs(obj.right_border - self.left_border) + 1
        elif direction == gamenames_.RIGHT:
            self.x -= abs(self.right_border - obj.left_border) + 1
        else:
            pass

    def _in_horizontal_line_with(self, obj):
        return not (obj.down_border < self.up_border or self.down_border < obj.up_border)

    def _in_vertical_line_with(self, obj):
        return not (obj.right_border < self.left_border or self.right_border < obj.left_border)

    def _in_collision_with(self, obj):
        return self._in_horizontal_line_with(obj) and self._in_vertical_line_with(obj)

    def _objects_array(self):
        for obj_list in self.classes.values():
            for obj in obj_list:
                yield obj

    # empty methods
    def _rotate_form(self, direction):
        pass

    def _action_after_collision(self, obj):
        pass

    # abstract methods
    def action(self):
        raise NotImplementedError
