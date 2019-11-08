# -*- coding: utf-8 -*-

__author__ = 'sebastian kihle', 'andreas sandvik hoimyr'
__email__ = 'sebaskih@nmbu.no', 'andrehoi@nmbu.no'

import random

class Board:

    def __init__(self, ladders=([1, 40],[9, 11],[37, 53],[44, 63],[50, 80],
                                [66, 83],[69, 86]),
                 chutes=([25, 6],[34, 4],[43, 31],[57, 38],[65, 28],[75, 13],
                         [88,71]), goal=90):
        self.board = []
        for tiles in range(96):
            self.board.append([tiles, 0])
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
                return chute[1]

        for ladder in self.ladders:
            if ladder[0] == position:
                return ladder[1]
        return position


class Player:
    def __init__(self, board):
        self.board = board
        self.position = 0

    def move(self):
        thorw_die = random.randint(1, 6)
        self.position += thorw_die
        self.board.position_adjustment(self.position)

class ResilientPlayer(Player):
    def __init__(self, board, add_move=1):
        super().__init__(board)
        self.add_move = add_move

    def move_resilient(self):




