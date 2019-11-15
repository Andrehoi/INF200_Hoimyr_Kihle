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
        self.counter = 0

    def move(self):
        throw_die = random.randint(1, 6)
        self.position += throw_die
        self.counter += 1
        self.position += self.board.position_adjustment(self.position)

    def step_counter(self):
        return self.counter


class ResilientPlayer(Player):
    def __init__(self, board, extra_steps=1):
        super().__init__(board)
        self.add_move = extra_steps
        self.chuted = False
        self.counter = 0

    def move(self):

        self.position += random.randint(1, 6)
        self.counter += 1
        move_adjustment = self.board.position_adjustment(self.position)
        self.position += move_adjustment

        if self.chuted:
            self.position += self.add_move
            self.chuted = False

        if move_adjustment < 0:
            self.chuted = True

    def step_counter(self):
        return self.counter


class LazyPlayer(Player):
    def __init__(self, board, dropped_steps=1):
        super().__init__(board)
        self.red_move = dropped_steps
        self.laddered = False
        self.counter = 0

    def move(self):

        throw_die = random.randint(1, 6)
        self.position += throw_die
        self.counter += 1

        move_adjustment = self.board.position_adjustment(self.position)
        self.position += move_adjustment

        if self.laddered:
            if self.red_move < throw_die:
                self.position -= self.red_move
            else:
                self.position -= throw_die

            self.laddered = False

        if move_adjustment > 0:
            self.laddered = True

    def step_counter(self):
        return self.counter


class Simulation:
    def __init__(self, player_field=[Player, LazyPlayer],
                 board=Board(), seed=3, randomize_players=True):
        self.board = board
        self.seed = random.seed(seed)
        self.game_list = []

        self.players = []
        for classes in player_field:
            player = classes(self.board)
            self.players.append(player)

        if randomize_players:
            random.shuffle(self.players)

    def single_game(self):
        while True:
            for p in self.players:
                p.move()
                # Check winning condition
                if self.board.goal_reached(p.position):
                    # reset the step counters and positions for all players
                    for i in self.players:
                        i.position = 0
                        steps = i.counter
                        i.counter = 0
                    return steps, type(p).__name__

    def run_simulation(self, n_games):
        for _ in range(n_games):
            self.game_list.append(self.single_game())

    def get_results(self):
        return self.game_list

    def winners_per_type(self):

        win_lazy = 0
        win_resilient = 0
        win_player = 0
        for steps in self.game_list:
            if 'Player' in steps:
                win_player += 1
            if 'LazyPlayer' in steps:
                win_lazy += 1
            if'ResilientPlayer' in steps:
                win_resilient += 1

        winner_dict = {'Player': win_player, 'LazyPlayer': win_lazy,
                       'ResilientPlayer': win_resilient}

        return winner_dict

    def durations_per_type(self):
        player_moves = []
        lazy_moves = []
        resilient_moves = []
        for steps in self.game_list:
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


sim = Simulation([Player, LazyPlayer, ResilientPlayer, LazyPlayer, Player])

sim.run_simulation(20)
print(sim.game_list)
print(sim.winners_per_type())
print(sim.durations_per_type())
print(sim.players_per_type())

