class Unit:
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage

    def decrease_health(self, value):
        self.health -= value
        if self.health <= 0:
            self.die()

    # abstract method
    def die(self):
        pass
