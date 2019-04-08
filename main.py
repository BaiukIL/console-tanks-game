"""Example of the game"""


import gamenames
import gameconfig
import player as player_mod
import game
import tank
import wall
import strategy
from getch import getch


def play_game():
    def create_field_borders():
        wall.Wall(x=0, y=0, height=gameconfig.FIELD_HEIGHT, width=1, game=this_game)
        wall.Wall(x=0, y=0, height=1, width=gameconfig.FIELD_WIDTH, game=this_game)
        wall.Wall(x=gameconfig.FIELD_WIDTH - 1, y=0, height=gameconfig.FIELD_HEIGHT, width=1, game=this_game)
        wall.Wall(x=0, y=gameconfig.FIELD_HEIGHT - 1, width=gameconfig.FIELD_WIDTH, height=1, game=this_game)

    def move_players():
        act = getch()
        this_game.main_player.action(act)
        for player in this_game.players.values():
            if player is not this_game.main_player:
                player.action(player.next_step)

    def move_other_movable_objects():
        for obj in this_game.groups[gamenames.MOVE_OBJECTS]:
            if not isinstance(obj, tank.Tank):
                obj.move()

    def game_loop():
        while True:
            this_game.draw_objects()
            this_game.field.update()
            move_players()
            move_other_movable_objects()

    this_game = game.Game()

    this_game.create_field(gameconfig.FIELD_WIDTH, gameconfig.FIELD_HEIGHT)
    create_field_borders()

    wall.Wall(30, 20, game=this_game, height=20, width=2)
    wall.Wall(30, 20, game=this_game, height=1, width=40)

    me = player_mod.Player("ilya", this_game)
    me.set_object(tank.Tank(x=1, y=1, speed_value=1, health=3, damage=1, game=this_game))
    this_game.add_player(me)

    enemy_1 = player_mod.Bot('enemy 1', this_game)
    enemy_1.set_strategy(strategy.square_path(side=20))
    enemy_1.set_object(tank.Tank(x=100, y=40, speed_value=1, health=3, damage=1, game=this_game))
    this_game.add_bot(enemy_1)

    enemy_2 = player_mod.Bot('enemy 2', this_game)
    enemy_2.set_strategy(strategy.square_path(side=50))
    enemy_2.set_object(tank.Tank(x=gameconfig.FIELD_WIDTH - 7, y=30, speed_value=1, health=3, damage=1, game=this_game))
    this_game.add_bot(enemy_2)

    enemy_3 = player_mod.Bot('enemy 3', this_game)
    enemy_3.set_strategy(strategy.static_shoot(10))
    enemy_3.set_object(tank.Tank(x=1, y=gameconfig.FIELD_HEIGHT - 4, speed_value=1, health=3, damage=1,
                                 game=this_game, start_direction=gamenames.UP))
    this_game.add_bot(enemy_3)

    game_loop()


if __name__ == '__main__':
    play_game()
