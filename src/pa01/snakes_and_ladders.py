# -*- coding: utf-8 -*-

__author__ = 'sebastian kihle', 'andreas sandvik hoimyr'
__email__ = 'sebaskih@nmbu.no', 'andrehoi@nmbu.no'

import random
import numpy as np


def make_board():
    """Creates the game board with the desired ladders and snakes"""
    num_tiles = [0 for i in range(96)]

    """Makes ladders"""
    num_tiles[1] = 39
    num_tiles[9] = 2
    num_tiles[37] = 16
    num_tiles[43] = 19
    num_tiles[49] = 30
    num_tiles[65] = 17
    num_tiles[68] = 17

    """Makes chutes"""
    num_tiles[24] = -19
    num_tiles[33] = -30
    num_tiles[42] = -12
    num_tiles[56] = -19
    num_tiles[64] = -37
    num_tiles[74] = -62
    num_tiles[87] = -17

    return num_tiles


def die_roll():
    """Rolls die between 1 and 6"""
    return random.randint(1, 6)


def player_turn(player, board):
    """Function that simulates one die throw for one player and move"""

    roll = die_roll()

    player[1] += roll + board[player[1] + roll]

    player[2] += 1

    return player


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
        print("Input is not a valid integer")
        raise TypeError

    if num_players > 8:
        print("maximum 8 players")
        return

    if num_players <= 0:
        print("mimimum 1 player")
        return

    board = make_board()
    players = ["PL1", "PL2", "PL3", "PL4", "PL5", "PL6", "PL7", "PL8"]

    game_players = players[:num_players]

    player_position = []

    for player in game_players:
        player_position.append([player, 0, 0])

    while True:
        for player in range(num_players):
            player_turn(player_position[player], board)

            if player_position[player][1] >= 90:
                return player_position[player][2]


print(single_game(8))


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
         List with the number of moves needed in each game.
     """

    if type(num_players) == int:
        pass

    else:
        print("Input is not a valid integer")
        raise ValueError

    if num_players > 8:
        print("maximum 8 players")
        return

    if num_players <= 0:
        print("mimimum 1 player")
        return

    moves = []
    for games in range(num_games):
        moves.append(single_game(num_players))

    return moves


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
        List with the number of moves needed in each game.
    """
    random.seed(seed)
    return multiple_games(num_games, num_players)


def median(data):
    """
    Returns median of data.

    :param data: An iterable of containing numbers
    :return: Median of data

    Source: https://github.com/yngvem/INF200-2019-Exercises/blob/master/
    exersices/ex03.rst
    """
    if len(data) < 1:
        raise ValueError

    sdata = sorted(data)
    n = len(sdata)
    return (sdata[n//2] if n % 2 == 1
            else 0.5 * (sdata[n//2 - 1] + sdata[n//2]))


if '__name__' == '__main__':
    games = multi_game_experiment(100, 4, random.randint())
    shortest_duration = min(games)
    longest_duration = max(games)
    median_duration = np.median(games)
    mean_duration = np.mean(games)
    standard_deviation = np.std(games)
    print()
