"""Example of the game"""


import gamenames_
import gameconfig_
import player_
import game_
import tank_
import wall_
import strategy_
from getch import getch


def play_game():
    def create_field_borders():
        wall_.Wall(x=0, y=0, height=gameconfig_.FIELD_HEIGHT, width=1, game=this_game)
        wall_.Wall(x=0, y=0, height=1, width=gameconfig_.FIELD_WIDTH, game=this_game)
        wall_.Wall(x=gameconfig_.FIELD_WIDTH - 1, y=0, height=gameconfig_.FIELD_HEIGHT, width=1, game=this_game)
        wall_.Wall(x=0, y=gameconfig_.FIELD_HEIGHT - 1, width=gameconfig_.FIELD_WIDTH, height=1, game=this_game)

    def move_players():
        act = getch()
        this_game.main_player.action(act)
        for player in this_game.players.values():
            if player is not this_game.main_player:
                player.action(player.next_step)

    def move_other_movable_objects():
        for obj in this_game.groups[gamenames_.MOVE_OBJECTS]:
            if not isinstance(obj, tank_.Tank):
                obj.move()

    def game_loop():
        while True:
            this_game.draw_objects()
            this_game.field.update()
            move_players()
            move_other_movable_objects()

    this_game.create_field(gameconfig_.FIELD_WIDTH, gameconfig_.FIELD_HEIGHT)
    create_field_borders()

    wall_.Wall(30, 20, game=this_game, height=20, width=2)
    wall_.Wall(30, 20, game=this_game, height=1, width=40)

    me = player_.Player("ilya", this_game)
    me.set_object(tank_.Tank(x=1, y=1, speed_value=1, health=3, damage=1, game=this_game))
    this_game.add_player(me)

    enemy_1 = player_.Bot('enemy 1', this_game)
    enemy_1.set_strategy(strategy_.square_path(side=20))
    enemy_1.set_object(tank_.Tank(x=100, y=30, speed_value=1, health=3, damage=1, game=this_game))
    this_game.add_bot(enemy_1)

    enemy_2 = player_.Bot('enemy 2', this_game)
    enemy_2.set_strategy(strategy_.square_path(side=50))
    enemy_2.set_object(tank_.Tank(x=gameconfig_.FIELD_WIDTH-7, y=30, speed_value=1, health=3, damage=1, game=this_game))
    this_game.add_bot(enemy_2)

    game_loop()


if __name__ == '__main__':
    this_game = game_.Game()
    play_game()
