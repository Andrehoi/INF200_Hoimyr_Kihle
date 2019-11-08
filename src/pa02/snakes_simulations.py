# -*- coding: utf-8 -*-

__author__ = 'sebastian kihle', 'andreas sandvik hoimyr'
__email__ = 'sebaskih@nmbu.no', 'andrehoi@nmbu.no'


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

    def position_adjustment(self):

        for pos in self.board:

            if not self.board[pos][1] == 0:
                if self.board[pos][0] in self.chutes:
                    self.board[self.chutes[pos][1]][0] = 1
                    self.board[pos][1] = 0




"""
ladders=([1, 40],[9, 11],[37, 53],[44, 63],[50, 80],
                                [66, 83],[69, 86]),
                 chutes=([25, 6],[34, 4],[43, 31],[57, 38],[65, 28],[75, 13],
                         [88,71]), goal=90)
"""

s = Board()

print(s.board)
