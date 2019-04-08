"""Module with players"""


import gamenames


class Player:
    def __init__(self, name, game):
        self.name = name
        self.obj = None
        self.game = game

    def set_object(self, obj):
        self.obj = obj

    # there is a problem: if object was removed from game (i. e. game doesn't have this object in its "classes")
    # player can still have reference to it. It happens because player.object reference to the very object so
    # removing it from game's scope doesn't influence to object's existence at all. Python's reference system doesn't
    # allow to have reference to the reference (e. g. "object" in game.classes is a such reference in this case)
    # To solve problem, I've decided to check if player.obj exists in game.classes every time it's called
    def exists(self):
        return self.obj in self.game.objects_array()

    def action(self, act):
        if not self.exists():
            return
        if act == 'w':
            self.obj.move(gamenames.UP)
        elif act == 'a':
            self.obj.move(gamenames.LEFT)
        elif act == 'd':
            self.obj.move(gamenames.RIGHT)
        elif act == 's':
            self.obj.move(gamenames.DOWN)
        elif act == ' ':
            self.obj.action()


class Bot(Player):
    def __init__(self, name, game):
        super().__init__(name, game)
        self.strategy = None

    def set_strategy(self, strategy):
        self.strategy = strategy

    @property
    def next_step(self):
        return self.strategy.__next__()