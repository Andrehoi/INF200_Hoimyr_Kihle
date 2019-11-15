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
        board = cs.Board()
        player = cs.Player(board)
        assert player.position == 0

    def test_player_moves(self):
        board = cs.Board()
        player = cs.Player(board)
        player.move()
        player.move()
        assert player.step_counter() == 2
        assert player.step_counter() >= 2

    def test_resilient_player_moves(self):
        board = cs.Board()
        player = cs.ResilientPlayer(board)
        player.move()
        player.move()
        assert player.step_counter() == 2
        assert player.step_counter() >= 2

    def test_resilience(self):
        board = cs.Board(chutes=([6, 1], [5, 1], [4, 1], [3, 1], [2, 1]))
        player = cs.ResilientPlayer(board, extra_steps=20)
        player.move()
        player.move()
        assert player.position >= 21
        player.move()
        assert player.position >= 27

    def test_lazy_player_moves(self):
        board = cs.Board()
        player = cs.LazyPlayer(board)
        player.move()
        player.move()
        assert player.step_counter() == 2
        assert player.step_counter() >= 2

    def test_laziness(self):
        board = cs.Board(ladders=([1, 10], [2, 10], [3, 10], [4, 10],
                                  [5, 10], [6, 10]))
        player = cs.LazyPlayer(board, dropped_steps=5)
        player.move()
        player.move()
        assert player.position <= 11
        player.move()
        assert player.position >= 11


class TestTheSimulator:

    def test_run_simulation(self):
        game_board = cs.Board()
        sim = cs.Simulation(board=game_board)
        sim.run_simulation(5)
        assert len(sim.game_list) == 5

    def test_winners_per_type(self):
        sim = cs.Simulation(player_field=[cs.Player, cs.Player,
                                          cs.Player])
        sim.run_simulation(3)
        the_dictionary = sim.winners_per_type()
        assert the_dictionary['Player'] == 3
        assert the_dictionary['ResilientPlayer'] == 0
        assert the_dictionary['LazyPlayer'] == 0

    def test_durations_per_type(self):
        sim = cs.Simulation(player_field=[cs.Player, cs.LazyPlayer,
                                          cs.ResilientPlayer])
        sim.run_simulation(5)
        the_dict = sim.durations_per_type()
        values = the_dict.values()
        for lists in values:
            for numbers in lists:
                assert numbers >= 4

    def test_players_per_type(self):
        sim = cs.Simulation(player_field=[cs.Player, cs.LazyPlayer,
                                          cs.ResilientPlayer, cs.LazyPlayer,
                                          cs.ResilientPlayer, cs.LazyPlayer])
        the_dict = sim.players_per_type()
        assert the_dict['Player'] == 1
        assert the_dict['ResilientPlayer'] == 2
        assert the_dict['LazyPlayer'] == 3













