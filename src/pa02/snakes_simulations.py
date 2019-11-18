# -*- coding: utf-8 -*-

__author__ = 'sebastian kihle', 'andreas sandvik hoimyr'
__email__ = 'sebaskih@nmbu.no', 'andrehoi@nmbu.no'

import random


class Board:
    """
    Class that represents the board
    """
    def __init__(self, ladders=([1, 40], [9, 11], [37, 53], [44, 63], [50, 80],
                                [66, 83], [69, 86]),
                 chutes=([25, 6], [34, 4], [43, 31], [57, 38], [65, 28],
                         [75, 13], [88, 71]), goal=90):
        self.ladders = ladders
        self.chutes = chutes
        self.goal = goal

    def goal_reached(self, position):
        """
        Checks the win condition, and returns boolean expression
        """
        if position >= self.goal:
            return True
        return False

    def position_adjustment(self, position):
        """
        Checks if the player is on a ladder or a chute, and returns the
        number of steps needed forwards or backwards
        """
        # Checks if the position is a chute
        for chute in self.chutes:
            if chute[0] == position:
                # Returns required steps back
                return chute[1] - chute[0]

        # Checks if the position is a ladder
        for ladder in self.ladders:
            if ladder[0] == position:
                # Returns the required steps forward
                return ladder[1] - ladder[0]
        # Returns 0 if not on a ladder or chute
        return 0


class Player:
    """
    Class that represents the players
    """
    def __init__(self, board):
        self.board = board
        self.position = 0
        self.counter = 0

    def move(self):
        """
        The move method for the player, which moves according to a die roll
        anc checks for chutes and ladders, and counts the number of moves
        """
        throw_die = random.randint(1, 6)
        self.position += throw_die
        self.counter += 1
        self.position += self.board.position_adjustment(self.position)

    def step_counter(self):
        """
        Returns the number of moves
        """
        return self.counter


class ResilientPlayer(Player):
    """
    Sub-class of player that represents a resilient player
    """
    def __init__(self, board, extra_steps=1):
        super().__init__(board)
        self.add_move = extra_steps
        self.chuted = False
        self.counter = 0

    def move(self):
        """
        Move method for the resilient player which will move some extra
        distance on the next throw if the player falls down a chute
        """
        self.position += random.randint(1, 6)
        self.counter += 1
        move_adjustment = self.board.position_adjustment(self.position)
        self.position += move_adjustment

        # Checks if the player fell down a chute last move
        if self.chuted:
            self.position += self.add_move
            self.chuted = False

        # Checks if the player has fallen down a chute this move
        if move_adjustment < 0:
            self.chuted = True

    def step_counter(self):
        """
        Returns the number of moves
        """
        return self.counter


class LazyPlayer(Player):
    """
    Sub-class of the player that represents the lazy player
    """
    def __init__(self, board, dropped_steps=1):
        super().__init__(board)
        self.red_move = dropped_steps
        self.laddered = False
        self.counter = 0

    def move(self):
        """
        Move method for the lazy player. The lazy player will move a reduced
        distance after going up a ladder in the next move
        """
        throw_die = random.randint(1, 6)
        self.position += throw_die
        self.counter += 1

        move_adjustment = self.board.position_adjustment(self.position)
        self.position += move_adjustment

        # Checks if the lazy player went up a ladder the last move
        if self.laddered:
            if self.red_move < throw_die:
                self.position -= self.red_move
            else:
                self.position -= throw_die

            self.laddered = False

        # Checks if the lazy player is going up a ladder this move
        if move_adjustment > 0:
            self.laddered = True

    def step_counter(self):
        """
        Returns the number of moves
        """
        return self.counter


class Simulation:
    """
    Class that simulates the snakes and ladders game with the player and
    board classes
    """
    def __init__(self, player_field=[Player, LazyPlayer],
                 board=Board(), seed=3, randomize_players=True):
        self.board = board
        self.seed = random.seed(seed)
        self.game_list = []

        # Applies the board class to each player
        self.players = []
        for classes in player_field:
            player = classes(self.board)
            self.players.append(player)

        # Randomizes the player order if True
        if randomize_players:
            random.shuffle(self.players)

    def single_game(self):
        """
        Play a single game of snakes and ladders. Moves all players until a
        player reaches the end of the board
        """
        steps = 0
        while True:
            for p in self.players:
                p.move()
                # Check winning condition
                if self.board.goal_reached(p.position):
                    # Reset the step counters and positions for all players
                    for player in self.players:
                        player.position = 0
                        steps = player.counter
                        player.counter = 0

                    return steps, type(p).__name__

    def run_simulation(self, n_games):
        """
        Plays several single games and adds all results to a list
        """
        for _ in range(n_games):
            self.game_list.append(self.single_game())

    def get_results(self):
        """
        Returns the results from the run simulation method
        """
        return self.game_list

    def winners_per_type(self):
        """
        Returns how many times each player won in the run simulation method
        as a dictionary
        """
        win_lazy = 0
        win_resilient = 0
        win_player = 0
        for steps in self.game_list:
            if 'Player' in steps:
                win_player += 1
            if 'LazyPlayer' in steps:
                win_lazy += 1
            if'ResilientPlayer' in steps:
                win_resilient += 1

        winner_dict = {'Player': win_player, 'LazyPlayer': win_lazy,
                       'ResilientPlayer': win_resilient}

        return winner_dict

    def durations_per_type(self):
        """
        Returns a dictionary with a list of how many moves the players used
        on each win
        """
        player_moves = []
        lazy_moves = []
        resilient_moves = []
        for steps in self.game_list:
            if 'Player' in steps:
                player_moves.append(steps[0])
            if 'LazyPlayer' in steps:
                lazy_moves.append(steps[0])
            if'ResilientPlayer' in steps:
                resilient_moves.append(steps[0])

        game_durations = {'Player': player_moves, 'LazyPlayer': lazy_moves,
                          'ResilientPlayer': resilient_moves}
        return game_durations

    def players_per_type(self):
        """
        Returns the number of each player type that were in the run
        simulation method
        """
        lazy_players = 0
        resilient_players = 0
        player_players = 0
        for player in self.players:
            if type(player).__name__ == 'Player':
                player_players += 1
            if type(player).__name__ == 'LazyPlayer':
                lazy_players += 1
            if type(player).__name__ == 'ResilientPlayer':
                resilient_players += 1

        the_dict = {'Player': player_players, 'LazyPlayer': lazy_players,
                    'ResilientPlayer': resilient_players}
        return the_dict
