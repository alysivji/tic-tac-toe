"""Tic-Tac-Toe Game"""

import itertools
import os

# Board Constants
NUM_ROWS = 3
NUM_COLS = 3
SEPARATOR = '---|---|---\n'

# Game Constants
GAME_PIECES = ['X', 'O']


def all_same(items):
    return all(x == items[0] for x in items)


class Board:
    """The board is made up of squares, stored as a mapping"""

    def __init__(self):
        """Set up board"""

        board = {}
        position_counter = 1

        for row in range(NUM_ROWS):
            for col in range(NUM_COLS):
                board[position_counter] = position_counter
                position_counter += 1

        self.board = board

    def add_position(self, slot, mark):
        if type(self.board[slot]) is int:
            self.board[slot] = mark
            return True
        return False

    def check_victory(self):
        """Maybe check victory or check if catz game
        Or check if we can continue, or have function to do something like this
        """
        pass

        # brute force it (maybe look at filter solution later)
        winning_combos = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9],
            [1, 5, 9],
            [3, 5, 7],
        ]

        for winning_combo in winning_combos:
            items = []
            for square in winning_combo:
                items.append(self.board[square])

            if all_same(items):
                print(f'{items[0]} wins!')
                return True

        return False

    def is_full(self):
        return set(self.board.values()) == set(['X', 'O'])

    def to_list(self):
        """Convert dictionary to list"""

        position_counter = 1
        board_list = []

        for row in range(NUM_ROWS):
            curr_row = []
            for col in range(NUM_COLS):
                curr_row.append(self.board[position_counter])
                position_counter += 1
            board_list.append(curr_row)

        return board_list

    def draw_board(self):
        """ASCII representation of game"""

        # convert board dictionary to board list

        board_text = ""

        for row in self.to_list():
            row_text = (' | '.join([str(square) for square in row]))
            board_text += f' {row_text}'
            board_text += '\n'
            board_text += SEPARATOR

        # remove last line
        board_text = board_text[:-len(SEPARATOR)]

        return board_text

    def __repr__(self):
        return self.draw_board()


class TicTacToe:
    """Game class which holds all game information"""

    def __init__(self):
        self.board = Board()
        self.game_pieces_cycle = itertools.cycle(GAME_PIECES)
        self.turn = next(self.game_pieces_cycle)

    def __repr__(self):
        return f'{self.board}'

    def next_turn(self):
        self.turn = next(self.game_pieces_cycle)

    def catz_game(self):
        return (not self.board.check_victory() and
                self.board.is_full())

    def check_victory(self):
        return self.board.check_victory()

    def player_turn(self, position):
        """Walk thru the process of a player's turn"""
        try:
            position = int(position)
        except ValueError:
            return (False, 'Please enter a number')

        if not (1 <= position <= 9):
            return (False, 'Please enter a valid position (1-9)')

        if not self.board.add_position(position, self.turn):
            return (False, 'Position is already taken, try again')

        return (True, 'All good')

    def restart(self):
        self.board = Board()
        self.turn = GAME_PIECES[0]


if __name__ == '__main__':
    game = TicTacToe()

    # Game Loop
    while True:
        # GUI
        os.system('cls' if os.name == 'nt' else 'clear')
        print(game)
        print(f"{game.turn}'s turn.")

        # Actual Game Loop
        pos = input('Enter a position: ')
        success, msg = game.player_turn(pos)
        if not success:
            print(msg)
            continue

        if game.check_victory():
            break

        game.next_turn()
