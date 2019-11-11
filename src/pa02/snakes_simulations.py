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

    def goal_reached(self, *args):
        if args is not None:
            return True
        return not self.board[self.goal][1] == 0

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

    def move(self):
        thorw_die = random.randint(1, 6)
        self.position += thorw_die
        self.poistion += self.board.position_adjustment(self.position)
        self.board.sheet[self.position][1] = 1


class ResilientPlayer(Player):
    def __init__(self, board, extra_steps=1):
        super().__init__(board)
        self.add_move = extra_steps
        self.chuted = False

    def move(self):

        self.position += random.randint(1, 6)
        self.position += self.board.position_adjustment(self.position)
        if self.chuted:
            self.position += self.add_move
            self.chuted = False

        if self.board.position_adjustment(self.position) < 0:
            self.chuted = True


class LazyPlayer(Player):
    def __init__(self, board, dropped_steps=1):
        super().__init__(board)
        self.red_move = dropped_steps
        self.laddered = False

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

        if self.position_adjustment() > 0:
            self.laddered = True


class Simulation:
    def __init__(self, *players, randomize_players=True):
        self.players = [players]
        self.lazy = LazyPlayer(Board())
        self.resilient = ResilientPlayer(Board())
        self.play = Player(Board())

    def single_game(self):
        lazy_counter = 0
        resilient_counter = 0
        player_counter = 0
        while True:
            for player in self.players:

                if isinstance(type(player), type(self.lazy)):
                    player.move()
                    lazy_counter += 1
                    if player.goal_reached():
                        return 'LazyPlayer', lazy_counter

                if isinstance(type(player), type(self.resilient)):
                    player.move()
                    resilient_counter += 1
                    if player.goal_reached():
                        return 'ResilientPlayer', resilient_counter

                if isinstance(type(player), type(self.play)):
                    player.move()
                    player_counter += 1
                    if player.goal_reached():
                        return 'Player', player_counter

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
