# -*- coding: utf-8 -*-

__author__ = 'sebastian kihle', 'andreas sandvik hoimyr'
__email__ = 'sebaskih@nmbu.no', 'andrehoi@nmbu.no'

import pytest
import snakes_simulations as cs


class TestTheBoard:

    def test_standard_board_setting(self):
        board = cs.Board()
        assert board.ladders == ([1, 40], [9, 11], [37, 53], [44, 63],
                                 [50, 80], [66, 83], [69, 86])

    def test_goal_reached(self):
        board = cs.Board(goal=95)
        if board.goal_reached(94):
            assert False
        if board.goal_reached(95):
            assert True

    def test_position_adjustment(self):
        board = cs.Board(ladders=([1, 21], [15, 25]), chutes=([40, 10],
                                                              [90, 1]))
        assert board.position_adjustment(1) == 20
        assert board.position_adjustment(90) == -89


class TestThePlayer:

    def test_player_starts_at_0(self):
        board = cs.Board
        player = cs.Player(board)
        assert player.position == 0

    def test_player_move_counter(self):
        board = cs.Board
        player = cs.Player(board)
        player.move()
        player.move()
        assert player.step_counter() > 2








