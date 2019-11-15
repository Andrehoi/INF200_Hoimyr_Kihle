# -*- coding: utf-8 -*-

__author__ = 'sebastian kihle', 'andreas sandvik hoimyr'
__email__ = 'sebaskih@nmbu.no', 'andrehoi@nmbu.no'

import random


class Board:

    def __init__(self, ladders=([1, 40], [9, 11], [37, 53], [44, 63], [50, 80],
                                [66, 83], [69, 86]),
                 chutes=([25, 6], [34, 4], [43, 31], [57, 38], [65, 28],
                         [75, 13], [88, 71]), goal=90):
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
                return ladder[1] - ladder[0]
        return 0


class Player:
    def __init__(self, board):
        self.board = board
        self.position = 0
        self.player_counter = 0

    def move(self):
        thorw_die = random.randint(1, 6)
        self.player_counter += 1
        self.position += thorw_die
        self.position += self.board.position_adjustment(self.position)

    def step_counter(self):
        return self.player_counter


class ResilientPlayer(Player):
    def __init__(self, board, extra_steps=1):
        super().__init__(board)
        self.add_move = extra_steps
        self.chuted = False
        self.resilient_counter = 0

    def move(self):

        self.position += random.randint(1, 6)
        self.resilient_counter += 1
        move_adjustment = self.board.position_adjustment(self.position)
        self.position += move_adjustment

        if self.chuted:
            self.position += self.add_move
            self.chuted = False

        if move_adjustment < 0:
            self.chuted = True

    def step_counter(self):
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
        self.lazy_counter += 1

        move_adjustment = self.board.position_adjustment(self.position)
        self.position += move_adjustment

        if self.laddered:
            if self.red_move < throw_die:
                self.position -= self.red_move
                self.laddered = False
            else:
                self.position -= throw_die

        if move_adjustment > 0:
            self.laddered = True

    def step_counter(self):
        self.lazy_counter += 1
        return self.lazy_counter


class Simulation:
    def __init__(self, player_field=[Player, LazyPlayer],
                 board=Board(), seed=3, randomize_players=True):
        self.board = board
        self.seed = random.seed(seed)
        self.gamelist = []

        self.players = []
        for classes in player_field:
            player = classes(self.board)
            self.players.append(player)

        if randomize_players:
            pass

    def single_game(self):
        while True:
            for p in self.players:
                p.move()

                if self.board.goal_reached(p.position):
                    return p.step_counter(), type(p).__name__

    def run_simulation(self, n_games):
        for _ in range(n_games):
            self.gamelist.append(self.single_game())

    def get_results(self):
        return self.gamelist

    def winners_per_type(self):
        win_player = self.gamelist.count('Player')
        win_lazy = self.gamelist.count('LazyPlayer')
        win_resilient = self.gamelist.count('ResilientPlayer')
        winner_dict = {'Player': win_player, 'LazyPlayer': win_lazy,
                       'ResilientPlayer': win_resilient}
        return winner_dict

    def durations_per_type(self):
        player_moves = []
        lazy_moves = []
        resilient_moves = []
        for steps in self.gamelist:
            if 'Player' in steps:
                player_moves.append(steps[0])
            if 'LazyPlayer' in steps:
                lazy_moves.append(steps[0])
            if'ResilientPlayer' in steps:
                resilient_moves.append(steps[0])

        game_durations = {'Player': player_moves, 'LazyPlayer': lazy_moves,
                          'ResilientPlayer': resilient_moves}
        return game_durations

    def players_per_type(self):
        return {'Player': self.players.count('Player'),
                'LazyPlayer': self.players.count('LazyPlayer'),
                'ResilientPlayer': self.players.count('ResilientPlayer')}


sim = Simulation([LazyPlayer, ResilientPlayer, Player])


print(sim.single_game())
sim.run_simulation(100)
print(sim.get_results())
print(sim.durations_per_type())
print(sim.players_per_type())
