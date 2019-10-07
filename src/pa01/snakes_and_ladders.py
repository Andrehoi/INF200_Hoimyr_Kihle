# -*- coding: utf-8 -*-

__author__ = 'sebastian kihle', 'andreas sandvik hoimyr'
__email__ = 'sebaskih@nmbu.no', 'andrehoi@nmbu.no'

import random

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


print(make_board())


def die_roll():
    """Rolls die between 1 and 6"""
    return random.randint(1,6)


def player_turn(player, board):
    if die_rolls == 0:
        pos = 0

    else:
        pass


    board[die_roll() + board[pos]] = player
    die_rolls += 1
    return board, die_rolls


print(player_turn('a', make_board()))


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
        raise ValueError

    if num_players > 8:
        print("maximum 8 players")
        return

    if num_players <= 0:
        print("mimimum 1 player")
        return



    players = ["a", "b", "c", "d", "e", "f", "g", "h"]

    game_players = players[:num_players]

    board = make_board()

    for player in game_players:
        player = player_turn(player)


    return (game_players)



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
