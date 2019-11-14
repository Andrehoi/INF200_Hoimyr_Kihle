# -*- coding: utf-8 -*-

__author__ = 'sebastian kihle', 'andreas sandvik hoimyr'
__email__ = 'sebaskih@nmbu.no', 'andrehoi@nmbu.no'

import random

class Board:

    def __init__(self, ladders=([1, 40], [9, 11], [37, 53], [44, 63], [50, 80],
                                [66, 83], [69, 86]),
                 chutes=([25, 6], [34, 4], [43, 31], [57, 38], [65, 28],
                         [75, 13], [88, 71]), goal=90):
        self.sheet = []
        for tiles in range(96):
            self.sheet.append([tiles, 0])
        self.ladders = ladders
        self.chutes = chutes
        self.goal = goal

    def goal_reached(self, position):
        if position >= self.goal:
            return True
        return False

    def position_adjustment(self, position):
        for chute in self.chutes:
            if chute[0] == position:
                return chute[1] - chute[0]

        for ladder in self.ladders:
            if ladder[0] == position:
                return ladder[1] - chute[0]
        return 0


class Player:
    def __init__(self, board):
        self.board = board
        self.position = 0
        self.player_counter = 0

    def move(self):
        thorw_die = random.randint(1, 6)
        self.position += thorw_die
        self.position += self.board.position_adjustment(self.position)


    def step_counter(self):
        self.player_counter += 1
        return self.player_counter


class ResilientPlayer(Player):
    def __init__(self, board, extra_steps=1):
        super().__init__(board)
        self.add_move = extra_steps
        self.chuted = False
        self.resilient_counter = 0

    def move(self):

        self.position += random.randint(1, 6)
        self.position += self.board.position_adjustment(self.position)
        if self.chuted:
            self.position += self.add_move
            self.chuted = False

        if self.board.position_adjustment(self.position) < 0:
            self.chuted = True

    def step_counter(self):
        self.resilient_counter += 1
        return self.resilient_counter


class LazyPlayer(Player):
    def __init__(self, board, dropped_steps=1):
        super().__init__(board)
        self.red_move = dropped_steps
        self.laddered = False
        self.lazy_counter = 0

    def move(self):
        throw_die = random.randint(1, 6)
        self.position += throw_die
        self.position += self.board.position_adjustment(self.position)
        if self.laddered:
            if self.red_move < throw_die:
                self.position -= self.red_move
                self.laddered = False
        else:
            self.position -= throw_die

        if self.board.position_adjustment(self.position) > 0:
            self.laddered = True

    def step_counter(self):
        self.lazy_counter += 1
        return self.lazy_counter


class Simulation:
    def __init__(self, player_field=[Player(), LazyPlayer()],
                 board=Board(), seed=0,
                 randomize_players=True):
        self.players = player_field
        self.board = board
        self.lazy = LazyPlayer(Board())
        self.resilient = ResilientPlayer(Board())
        self.play = Player(Board())
        self.seed = random.seed(seed)

        if randomize_players:
            random.shuffle(self.players)

    def single_game(self):

        while False:
            for player in self.players:

                player.move()
                player.step_counter()

                if board.goal_reached(player.position):
                    return print(' Player {0} wins in {1} moves'.format(
                        player, player.step_counter))


    def run_simulation(self):
        pass

    def get_results(self):
        pass

    def winners_per_type(self):
        pass

    def durations_per_type(self):
        pass

    def players_per_type(self):
        pass


sim = Simulation(LazyPlayer, Player)
print(sim.single_game())
