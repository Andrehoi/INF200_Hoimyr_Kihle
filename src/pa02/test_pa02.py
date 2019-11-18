# -*- coding: utf-8 -*-

__author__ = 'sebastian kihle', 'andreas sandvik hoimyr'
__email__ = 'sebaskih@nmbu.no', 'andrehoi@nmbu.no'

import snakes_simulations as cs


class TestTheBoard:
    """
    Test class for the board
    """

    def test_standard_board_setting(self):
        """
        Tests the default bord chutes and ladders is correct
        """
        board = cs.Board()
        assert board.ladders == ([1, 40], [9, 11], [37, 53], [44, 63],
                                 [50, 80], [66, 83], [69, 86])

    def test_goal_reached(self):
        """
        Tests that the goal reached method works
        """
        board = cs.Board(goal=95)
        if board.goal_reached(94):
            assert False
        if board.goal_reached(95):
            assert True

    def test_position_adjustment(self):
        """
        Checks that the position adjustment returns the difference between
        the chute and ladder exit/entry
        """
        board = cs.Board(ladders=([1, 21], [15, 25]), chutes=([40, 10],
                                                              [90, 1]))
        assert board.position_adjustment(1) == 20
        assert board.position_adjustment(90) == -89


class TestThePlayer:
    """
    Test class for the players
    """

    def test_player_starts_at_0(self):
        """
        Checks that the players starts in position 0
        """
        board = cs.Board()
        player = cs.Player(board)
        assert player.position == 0

    def test_player_moves(self):
        """
        Checks that the step counter works
        """
        board = cs.Board()
        player = cs.Player(board)
        player.move()
        player.move()
        assert player.step_counter() == 2

    def test_resilient_player_moves(self):
        """
        Check that the resilient player step counter works
        """
        board = cs.Board()
        player = cs.ResilientPlayer(board)
        player.move()
        player.move()
        assert player.step_counter() == 2

    def test_resilience(self):
        """
        Checks that the resilient player moves extra steps after falling
        down a chute in the next move
        """
        board = cs.Board(chutes=([6, 1], [5, 1], [4, 1], [3, 1], [2, 1]))
        player = cs.ResilientPlayer(board, extra_steps=20)
        player.move()
        player.move()
        assert player.position >= 21
        player.move()
        assert player.position >= 27

    def test_lazy_player_moves(self):
        """
        Checks that the lazy player step counter works
        """
        board = cs.Board()
        player = cs.LazyPlayer(board)
        player.move()
        player.move()
        assert player.step_counter() == 2

    def test_laziness(self):
        """
        Checks that the lazy player moves shorter after going up a ladder
        """
        board = cs.Board(ladders=([1, 10], [2, 10], [3, 10], [4, 10],
                                  [5, 10], [6, 10]))
        player = cs.LazyPlayer(board, dropped_steps=5)
        player.move()
        player.move()
        assert player.position <= 11
        player.move()
        assert player.position >= 11


class TestTheSimulator:
    """
    Test class for the simulator
    """

    def test_run_simulation(self):
        """
        Checks that the length of the list for the run simulation method is
        5 after running 5 games
        """
        game_board = cs.Board()
        sim = cs.Simulation(board=game_board)
        sim.run_simulation(5)
        assert len(sim.game_list) == 5

    def test_winners_per_type(self):
        """
        Checks that the winners per type method counts the right amout of
        winners
        """
        sim = cs.Simulation(player_field=[cs.Player, cs.Player,
                                          cs.Player])
        sim.run_simulation(3)
        the_dictionary = sim.winners_per_type()
        assert the_dictionary['Player'] == 3
        assert the_dictionary['ResilientPlayer'] == 0
        assert the_dictionary['LazyPlayer'] == 0

    def test_durations_per_type(self):
        """
        Checks that no players win in less than 4 moves, which shouldn't be
        possible
        """
        sim = cs.Simulation(player_field=[cs.Player, cs.LazyPlayer,
                                          cs.ResilientPlayer])
        sim.run_simulation(5)
        the_dict = sim.durations_per_type()
        values = the_dict.values()
        for lists in values:
            for numbers in lists:
                assert numbers >= 4

    def test_players_per_type(self):
        """
        Checks that the players per type method correctly counts the amount
        of each player
        """
        sim = cs.Simulation(player_field=[cs.Player, cs.LazyPlayer,
                                          cs.ResilientPlayer, cs.LazyPlayer,
                                          cs.ResilientPlayer, cs.LazyPlayer])
        the_dict = sim.players_per_type()
        assert the_dict['Player'] == 1
        assert the_dict['ResilientPlayer'] == 2
        assert the_dict['LazyPlayer'] == 3
