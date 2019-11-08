# -*- coding: utf-8 -*-

__author__ = 'sebastian kihle', 'andreas sandvik hoimyr'
__email__ = 'sebaskih@nmbu.no', 'andrehoi@nmbu.no'


class Board:

    def __init__(self, *ladders, *chutes):

        self.board = []
        for tiles in range(96):
            self.board.append([tiles, 0])

        self.ladders = ladders
        self.chutes = chutes

    def goal_reached(self):

        if _ is True:
            return True
        else:
            return False

    def position_adjustment(self):
        pass

s = Board()

print(s.board)