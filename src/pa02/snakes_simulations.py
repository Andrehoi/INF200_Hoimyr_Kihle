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




    def goal_reached(self):

        if _ is True:
            return True
        else:
            return False

    def position_adjustment(self):
        pass

