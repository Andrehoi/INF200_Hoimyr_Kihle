# -*- coding: utf-8 -*-

__author__ = 'sebastian kihle', 'andreas sandvik hoimyr'
__email__ = 'sebaskih@nmbu.no', 'andrehoi@nmbu.no'



def make_board():
    """Creates the game board with the desired ladders and snakes"""
    num_tiles = [0 for i in range(96)]

    num_tiles[1] = 39
    num_tiles[9] = 2
    num_tiles[37] = 16
    num_tiles[43] = 19
    num_tiles[49] = 30
    num_tiles[65] = 17
    num_tiles[68] = 17

    num_tiles[24] = -19
    num_tiles[33] = -30
    num_tiles[42] = -12
    num_tiles[56] = -19
    num_tiles[64] = -37
    num_tiles[74] = -62
    num_tiles[87] = -17

    return num_tiles


print(make_board())



def single_game(num_players):

    """
    Returns duration of single game.

    Arguments
    ---------
    num_players : int
        Number of players in the game

    Returns
    -------
    num_moves : int
        Number of moves the winning player needed to reach the goal
    """

    if type(num_players) == int:
        pass

    else:
        raise ValueError



def multiple_games(num_games, num_players):
    """
    Returns durations of a number of games.

    Arguments
    ---------
    num_games : int
        Number of games to play
    num_players : int
        Number of players in the game

    Returns
    -------
    num_moves : list
        List with the numbedr of moves needed in each game.
    """

def multi_game_experiment(num_games, num_players, seed):
    """
    Returns durations of a number of games when playing with given seed.

    Arguments
    ---------
    num_games : int
        Number of games to play
    num_players : int
        Number of players in the game
    seed : int
        Seed used to initialise the random number generator

    Returns
    -------
    num_moves : list
        List with the numbedr of moves needed in each game.
    """
